from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomResponse
from typing import List

router = APIRouter(prefix="/rooms", tags=["Rooms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=List[RoomResponse],
    summary="Listar habitaciones",
    description="Retorna la lista completa de habitaciones disponibles en el hotel."
)
def get_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()

@router.get(
    "/{room_id}",
    response_model=RoomResponse,
    summary="Obtener habitación por ID",
    description="Retorna los detalles de una habitación específica según su ID."
)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return room

@router.post(
    "/",
    response_model=RoomResponse,
    summary="Crear habitación",
    description="Crea una nueva habitación en el sistema con nombre, tipo, precio y descripción."
)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    new_room = Room(**room.model_dump())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@router.put(
    "/{room_id}",
    response_model=RoomResponse,
    summary="Actualizar habitación",
    description="Actualiza los datos de una habitación existente según su ID."
)
def update_room(room_id: int, room: RoomCreate, db: Session = Depends(get_db)):
    existing = db.query(Room).filter(Room.id == room_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    for key, value in room.model_dump().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete(
    "/{room_id}",
    status_code=204,
    summary="Eliminar habitación",
    description="Elimina permanentemente una habitación del sistema según su ID."
)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    db.delete(room)
    db.commit()