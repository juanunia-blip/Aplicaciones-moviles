from pydantic import BaseModel

class RoomBase(BaseModel):
    nombre: str
    tipo: str
    precio: float
    descripcion: str

    model_config = {
        "from_attributes": True
    }

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int

    class ConfigDict:
        from_attributes = True

