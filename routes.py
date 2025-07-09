from fastapi import APIRouter, HTTPException, Query, Body
from schema import FitnessClass, BookingRequest
from typing import List
import uuid
import logging
from db import read_data, write_data
from utils import convert_timezone

logging.basicConfig(level=logging.INFO)
router = APIRouter()

@router.get("/classes", response_model=List[FitnessClass])
def get_classes(timezone:str = 'Asia/Kolkata'):
    logging.info(f"Reading data from db")
    data = read_data()
    classes = data.get("classes", [])

    converted = []

    logging.info(f"Converting class times to timezone: {timezone}")    
    for c in classes:
        convertedTime = convert_timezone(c["datetime"], timezone)
        if not convertedTime:
            raise HTTPException(status_code=400, detail='Invalid Timezone given')
        c["datetime"] = convertedTime
        logging.info(f"Adding class: {c['name']} to response")
        converted.append(c)
    logging.info(f"Returning {len(converted)} classes")
    return converted

@router.post("/book")
def book_class(payload:BookingRequest = Body(...)):
    logging.info(f"Reading data from db for booking")
    data = read_data()
    classes = data.get("classes", [])
    bookings = data.get("bookings", [])

    selected_class = next((c for c in classes if c["id"] == payload.class_id), None)

    if not selected_class:
        logging.error(f"Class with id {payload.class_id} not found")
        raise HTTPException(status_code=404, detail='class not found')
    
    if selected_class["available_slots"] <= 0:
        logging.error(f"No available slots for class {payload.class_id}")
        raise HTTPException(status_code=404, detail='No slots are available')

    selected_class["available_slots"] -= 1

    logging.info(f"Booking class {payload.class_id} for {payload.client_name}")
    booking = {
        "id": str(uuid.uuid4()),
        "class_id": payload.class_id,
        "client_name": payload.client_name,
        "client_email": payload.client_email
    }

    bookings.append(booking)
    data["classes"] = classes
    data["bookings"] = bookings

    logging.info(f"Writing updated data to db")
    write_data(data)

    logging.info(f"Booking successful with id {booking['id']}")
    return {"message": "Booking successful", "booking_id": booking["id"]}


@router.get("/bookings")
def get_bookings_by_email(email: str = Query(...)):
    logging.info(f"Fetching bookings for email: {email}")
    data = read_data()
    bookings = data.get("bookings")
    user_bookings = [c for c in bookings if c["client_email"] == email ]
    if not user_bookings:
        logging.error(f"No bookings found for email: {email}")
        raise HTTPException(status_code=400, detail='No bookings made')
    logging.info(f"Found {len(user_bookings)} bookings for email: {email}")
    return {"email":email, "bookings":user_bookings}