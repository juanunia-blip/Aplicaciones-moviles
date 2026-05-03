from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

    model_config = {"from_attributes": True}

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str

    model_config = {
        "from_attributes": True
    }