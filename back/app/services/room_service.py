from sqlalchemy.orm import Session
from app.models.room import Room

def create_room(db: Session, room):
    new_room = Room(**room.dict())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

def get_rooms(db: Session):
    return db.query(Room).all()