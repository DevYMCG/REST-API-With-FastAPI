from database import Base, engine
from models import Item

print("create database ....")

Base.metadata.create_all(engine)
