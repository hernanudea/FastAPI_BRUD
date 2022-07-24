from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    last_name: str
    address: Optional[str]
    phone: str
    created: datetime = datetime.now()


class UserId(BaseModel):
    id: int
