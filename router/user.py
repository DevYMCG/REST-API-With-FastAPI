from typing import List
from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session

from schemas import user as user_schema
from services import user_service

from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    summary="Create new user"
)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    get_user = user_service.get_user_by_email(db, email=user.email)
    if get_user:
        msg = "Email already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    return user_service.create_user(db=db, user=user)


@router.get(
    "/",
    response_model=List[user_schema.User]
)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@router.get(
    "/{user_id}",
    response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user