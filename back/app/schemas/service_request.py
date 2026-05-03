from pydantic import BaseModel
from typing import Optional

class ServiceRequestBase(BaseModel):
    tipo: str
    detalle: Optional[str] = None

class ServiceRequestCreate(ServiceRequestBase):
    pass

class ServiceRequestResponse(ServiceRequestBase):
    id: int
    estado: str

    class Config:
        from_attributes = True