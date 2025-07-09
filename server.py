from fastapi import FastAPI, HTTPException
from routes import router
from db import seed_data

app = FastAPI(title='Hey this is my Booking API Assignment')

@app.on_event("startup")
def startup_event():
    print("🔁 Seeding data on startup...")
    seed_data()
    print("✅ Seeding complete.")

@app.get("/")
def welcome():
    print("Welcome ready for booking your classes")

app.include_router(router)