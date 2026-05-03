from sqlalchemy import Column, Integer, String
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(String)
    fecha_fin = Column(String)
    adultos = Column(Integer)
    ninos = Column(Integer)
    estado = Column(String)
    room_id = Column(Integer)