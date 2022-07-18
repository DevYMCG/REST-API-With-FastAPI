from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import settings

settings = settings()

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping= True,
    echo= True
)

SessionLocal= sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()