from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse
from app.core.security import get_current_user
from typing import List

router = APIRouter(prefix="/bookings", tags=["Bookings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=List[BookingResponse],
    summary="Listar reservas",
    description="Retorna la lista completa de reservas registradas en el sistema."
)
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.get(
    "/{booking_id}",
    response_model=BookingResponse,
    summary="Obtener reserva por ID",
    description="Retorna los detalles de una reserva específica según su ID."
)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return booking

@router.post(
    "/",
    response_model=BookingResponse,
    summary="Crear reserva",
    description="Crea una nueva reserva. Requiere autenticación JWT. Asocia una habitación con fechas, adultos y niños."
)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    new_booking = Booking(**booking.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.put(
    "/{booking_id}",
    response_model=BookingResponse,
    summary="Actualizar reserva",
    description="Actualiza los datos de una reserva existente. Requiere autenticación JWT."
)
def update_booking(
    booking_id: int,
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    existing = db.query(Booking).filter(Booking.id == booking_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    for key, value in booking.model_dump().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing