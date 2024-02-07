from uuid import UUID

from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID


Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):  # type: ignore
    pass


class UserRead(BaseUser[UUID]):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(BaseUserUpdate):
    pass
