from fastapi import APIRouter, HTTPException, Query, Body
from schema import FitnessClass, BookingRequest
from typing import List
import uuid

from db import read_data, write_data
from utils import convert_timezone


router = APIRouter()

@router.get("/classes", response_model=List[FitnessClass])
def get_classes(timezone:str = 'Asia/Kolkata'):
    data = read_data()
    classes = data.get("classes", [])

    converted = []

    for c in classes:
        convertedTime = convert_timezone(c["datetime"], timezone)
        if not convert_timezone:
            raise HTTPException(status_code=400, detail='Invalid Timezone given')
        c["datetime"] = convertedTime
        converted.append(c)
    return converted

@router.post("/book")
def book_class(payload:BookingRequest = Body(...)):
    data = read_data()
    classes = data.get("classes", [])
    bookings = data.get("bookings", [])

    selected_class = next((c for c in classes if c["id"] == payload.class_id), None)

    if not selected_class:
        raise HTTPException(status_code=404, detail='class not found')
    
    if selected_class["available_slots"] <= 0:
        raise HTTPException(status_code=404, detail='No slots are available')

    selected_class["available_slots"] -= 1

    booking = {
        "id": str(uuid.uuid4()),
        "class_id": payload.class_id,
        "client_name": payload.client_name,
        "client_email": payload.client_email
    }

    bookings.append(booking)
    data["classes"] = classes
    data["bookings"] = bookings

    write_data(data)

    return {"message": "Booking successful", "booking_id": booking["id"]}


@router.get("/bookings")
def get_bookings_by_email(email: str = Query(...)):
    data = read_data()
    bookings = data.get("bookings")
    user_bookings = [c for c in bookings if c["client_email"] == email ]
    if not user_bookings:
        raise HTTPException(status_code=400, detail='No bookings made')
    return {"email":email, "bookings":user_bookings}