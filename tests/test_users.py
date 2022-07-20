from fastapi.testclient import TestClient
from database import SessionLocal as Session

import services as crud

from tests.utils.utils import random_email, random_lower_string
from src.settings import settings

from schemas.user import UserCreate

settings = settings()

def test_create_user_new_email(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    username = random_email()
    password = random_lower_string()
    data = {"email": username, "password": password}
    r = client.post(
        f"{settings.API_V1_STR}/users/", headers=superuser_token_headers, json=data,
    )
    assert 200 <= r.status_code < 300
    created_user = r.json()
    user = crud.user_service.get_user_by_email(db, email=username)
    assert user
    assert user.email == created_user["email"]

def test_get_existing_user(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    user = crud.user_service.create_user(db, user=user_in)
    user_id = user.id
    r = client.get(
        f"{settings.API_V1_STR}/users/{user_id}", headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = crud.user_service.get_user_by_email(db, email=username)
    assert existing_user
    assert existing_user.email == api_user["email"]