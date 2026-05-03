from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tipo = Column(String)
    precio = Column(Float)
    descripcion = Column(String)