from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }