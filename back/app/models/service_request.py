from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class ServiceRequest(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(80), nullable=False)   # limpieza | room_service | toallas
    detalle = Column(String(300))
    estado = Column(String(30), default="pendiente")  # pendiente | en_proceso | resuelto
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())