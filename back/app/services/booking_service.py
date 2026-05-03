from sqlalchemy.orm import Session
from app.models.booking import Booking

def create_booking(db: Session, booking):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_bookings(db: Session):
    return db.query(Booking).all()