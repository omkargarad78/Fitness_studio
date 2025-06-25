from pydantic import BaseModel,EmailStr,Field
from datetime import datetime
from typing import Annotated


class FitnessClassOut(BaseModel):
    id:int
    name:str
    instructor:str
    datetime:datetime
    available_slots:int

    class Config:
        orm_mode=True


class BookingRequest(BaseModel):
    class_id: Annotated[int, Field(..., description="ID of the class to book")]
    client_name: Annotated[str, Field(..., min_length=1, description="Name of the client")]
    client_email: Annotated[EmailStr, Field(..., description="Valid email of the client")]

class BookingOut(BaseModel):
    id:int
    class_id:int
    client_name:str
    client_email:EmailStr

    class Config:
        orm_mode=True
        