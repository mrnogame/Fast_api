from typing import Optional , List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum


class Gender (str,Enum):
    male = "male"
    female = "male"

class Role (str, Enum):
    admin = "admin"
    user ="User"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name : str
    middle_name : Optional[str]
    gender : Gender
    role : List[Role]


