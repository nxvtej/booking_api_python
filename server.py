from fastapi import FastAPI, HTTPException
from routes import router

app = FastAPI(title='Hey this is my Booking API Assignment')

@app.get("/")
def welcome():
    print("Welcome ready for booking your classes")

app.include_router(router)