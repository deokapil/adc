from typing import Optional

from pydantic import BaseModel

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    username: str
    password: str


class UserInCreate(UserInLogin):
    username: str
    name: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None


class UserWithToken(User):
    token: str


class UserInResponse(RWSchema):
    user: UserWithToken
