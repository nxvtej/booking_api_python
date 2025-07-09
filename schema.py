from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List


class FitnessClass(BaseModel):
    id:int
    name:str
    instructor:str
    datetime:datetime
    available_slots:int

class BookingRequest(BaseModel):
    id:int
    class_id:int
    client_name:str
    client_email:EmailStr