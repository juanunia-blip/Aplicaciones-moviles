from pydantic import BaseModel
from typing import Optional

class PlaceBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    lat: Optional[str] = None
    lon: Optional[str] = None
    #imagen_url: Optional[str] = None

class PlaceCreate(PlaceBase):
    pass

class PlaceResponse(PlaceBase):
    id: int

    class Config:
        from_attributes = True