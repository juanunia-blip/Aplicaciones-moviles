from pydantic import BaseModel

class BookingBase(BaseModel):
    fecha_inicio: str
    fecha_fin: str
    adultos: int
    ninos: int
    estado: str
    room_id: int

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int

    class Config:
        from_attributes = True