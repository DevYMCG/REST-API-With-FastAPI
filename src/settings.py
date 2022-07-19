import os

from pydantic import BaseSettings, EmailStr, PostgresDsn, validator
from typing import Optional, Dict, Any
from dotenv import load_dotenv
load_dotenv()

class settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES : int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

    POSTGRES_SERVER: str = os.getenv('DB_HOST')
    POSTGRES_USER: str = os.getenv('DB_USER')
    POSTGRES_PASSWORD: str = os.getenv('DB_PASS')
    POSTGRES_DB: str = os.getenv('DB_NAME')
    POSTGRES_PORT: str = os.getenv('DB_PORT')
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = 'postgresql://{}:{}@{}:{}/{}'.format(POSTGRES_USER,POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT,POSTGRES_DB)

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    EMAIL_TEST_USER: EmailStr = os.getenv('EMAIL_TEST_USER')  # type: ignore
    FIRST_SUPERUSER: EmailStr = os.getenv('FIRST_SUPERUSER')
    FIRST_SUPERUSER_PASSWORD: str = os.getenv('FIRST_SUPERUSER_PASSWORD')