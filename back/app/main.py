from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User
from app.models.room import Room
from app.models.booking import Booking
from app.models.place import Place
from app.models.service_request import ServiceRequest
from app.routes.auth_routes import router as auth_router
from app.routes.room_routes import router as rooms_router
from app.routes.booking import router as bookings_router
from app.routes.places import router as places_router
from app.routes.services import router as services_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="App Hotel Popayán API",
    description="Backend para la aplicación móvil Hotel Popayán",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(rooms_router)
app.include_router(bookings_router)
app.include_router(places_router)
app.include_router(services_router)

@app.get("/")
def root():
    return {"message": "Backend App Hotel Popayán en ejecución"}