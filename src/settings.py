import os

from pydantic import BaseSettings, PostgresDsn, validator
from typing import Optional, Dict, Any
from dotenv import load_dotenv
load_dotenv()

class settings(BaseSettings):

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

