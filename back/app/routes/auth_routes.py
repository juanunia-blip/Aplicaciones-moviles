from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.core.security import oauth2_scheme, decode_access_token
from app.services.auth_service import register_user, login_user, get_user_by_email

router = APIRouter(prefix="/auth", tags=["Autenticación"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = login_user(db, form_data.username, form_data.password)
    if not result:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return result

@router.get("/me", response_model=UserResponse)
def get_me(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user