from typing import List

from pydantic import BaseModel

from schemas import item

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[item.Item] = []

    class Config:
        orm_mode = True