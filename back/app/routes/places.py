from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.place import Place
from app.schemas.place import PlaceCreate, PlaceResponse

router = APIRouter(prefix="/places", tags=["Lugares turísticos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=List[PlaceResponse],
    summary="Listar lugares turísticos",
    description="Retorna todos los lugares turísticos de Popayán registrados en el sistema."
)
def get_places(db: Session = Depends(get_db)):
    return db.query(Place).all()

@router.get(
    "/{place_id}",
    response_model=PlaceResponse,
    summary="Obtener lugar por ID",
    description="Retorna los detalles de un lugar turístico específico según su ID."
)
def get_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return place

@router.post(
    "/",
    response_model=PlaceResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear lugar turístico",
    description="Registra un nuevo lugar turístico con nombre, descripción, categoría y coordenadas."
)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    new_place = Place(**place.model_dump())
    db.add(new_place)
    db.commit()
    db.refresh(new_place)
    return new_place

@router.put(
    "/{place_id}",
    response_model=PlaceResponse,
    summary="Actualizar lugar turístico",
    description="Actualiza los datos de un lugar turístico existente según su ID."
)
def update_place(place_id: int, place: PlaceCreate, db: Session = Depends(get_db)):
    existing = db.query(Place).filter(Place.id == place_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    for key, value in place.model_dump().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete(
    "/{place_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar lugar turístico",
    description="Elimina permanentemente un lugar turístico del sistema según su ID."
)
def delete_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    db.delete(place)
    db.commit()