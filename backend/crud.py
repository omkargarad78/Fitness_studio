from sqlalchemy.orm import Session
from .models import FitnessClass, Booking  
from .schemas import BookingRequest  
from fastapi import HTTPException

def get_all_classes(db: Session):
    return db.query(FitnessClass).filter(FitnessClass.available_slots > 0).all()

def book_class(request: BookingRequest, db: Session):
    cls = db.query(FitnessClass).filter(FitnessClass.id == request.class_id).first()
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    if cls.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    cls.available_slots -= 1
    booking = Booking(**request.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_email(email: str, db: Session):
    return db.query(Booking).filter(Booking.client_email == email).all()