from fastapi import FastAPI, HTTPException
from routes import router
from db import seed_data
from server import logging

app = FastAPI(title='Hey this is my Booking API Assignment')

@app.on_event("startup")
def startup_event():
    logging.info("🔁 Seeding data on startup...")
    seed_data()
    logging.info("✅ Seeding complete.")

@app.get("/")
def welcome():
    logging.info("Welcome ready for booking your classes")
    return {"message": "Welcome to the Fitness Class Booking API!"}

app.include_router(router)