from uuid import UUID

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from ..helpers.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class UserRead(BaseUser[UUID]):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(BaseUserUpdate):
    pass
