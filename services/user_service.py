from sqlalchemy.orm import Session

from fastapi import HTTPException, status


from models.user import User as UserModel
from schemas import user as user_schema
from services.auth_service import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    db_user = UserModel(
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
        is_superuser =user.is_superuser
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user