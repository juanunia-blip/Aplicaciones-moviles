from sqlalchemy import Column, Integer, String
from app.database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(500))
    categoria = Column(String(60))   # iglesia | parque | museo | restaurante
    lat = Column(String(20))
    lon = Column(String(20))
    imagen_url = Column(String(300))