from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.service_request import ServiceRequest
from app.schemas.service_request import ServiceRequestCreate, ServiceRequestResponse

router = APIRouter(prefix="/services", tags=["Servicios / Solicitudes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=List[ServiceRequestResponse],
    summary="Listar solicitudes de servicio",
    description="Retorna todas las solicitudes de servicio registradas en el sistema."
)
def get_services(db: Session = Depends(get_db)):
    return db.query(ServiceRequest).all()

@router.post(
    "/",
    response_model=ServiceRequestResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear solicitud de servicio",
    description="Registra una nueva solicitud de servicio como limpieza, room service o toallas."
)
def create_service(service: ServiceRequestCreate, db: Session = Depends(get_db)):
    new_service = ServiceRequest(**service.model_dump())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.put(
    "/{service_id}/estado",
    response_model=ServiceRequestResponse,
    summary="Actualizar estado de solicitud",
    description="Cambia el estado de una solicitud: pendiente → en_proceso → resuelto."
)
def update_estado(service_id: int, estado: str, db: Session = Depends(get_db)):
    service = db.query(ServiceRequest).filter(ServiceRequest.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    service.estado = estado
    db.commit()
    db.refresh(service)
    return service