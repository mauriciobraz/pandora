from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .dotenv import get_env_variable
from ..schemas.user_schemas import User

DATABASE_URL = get_env_variable(
    str,
    "DATABASE_URL",
    "sqlite+aiosqlite:///pandora.db",
)


engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(
    expire_on_commit=False,
    class_=AsyncSession,
    engine=engine,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


Base: DeclarativeMeta = declarative_base()


async def migrate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Getters


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
