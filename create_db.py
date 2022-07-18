from database import Base, engine
from models.item import Item
from models.user import User

print("create database ....")

Base.metadata.create_all(engine)
