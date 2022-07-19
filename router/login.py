from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from services import auth_service
from schemas.token import Token

from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/api/v1")

@router.post(
    "/login",
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    access_token = auth_service.generate_token(db=db, username=form_data.username, password=form_data.password)
    return {"access_token": access_token, "token_type": "bearer"}