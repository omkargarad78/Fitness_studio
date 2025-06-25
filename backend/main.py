from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/classes", response_model=list[schemas.FitnessClassOut])
def read_classes(db: Session = Depends(get_db)):
    return crud.get_all_classes(db)

@app.post("/book", response_model=schemas.BookingOut)
def book(request: schemas.BookingRequest, db: Session = Depends(get_db)):
    return crud.book_class(request, db)

@app.get("/bookings", response_model=list[schemas.BookingOut])
def bookings(email: str, db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(email, db)
