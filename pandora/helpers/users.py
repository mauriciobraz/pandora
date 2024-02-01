from uuid import UUID
from typing import Optional

from loguru import logger
from fastapi import Depends, Request

from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from .dotenv import get_env_variable
from .database import get_async_session, get_user_db

from ..schemas.user_schemas import User

JWT_SECRET = get_env_variable(
    str,
    "JWT_SECRET",
    "cc3b0103d9bec7969cf46613959083d6161602520e2e3f2566e645bb7b221a18",
)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    verification_token_secret = JWT_SECRET
    reset_password_token_secret = JWT_SECRET

    async def on_after_register(self, user: User, _: Optional[Request] = None):
        logger.debug(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, _: Optional[Request] = None
    ):
        logger.debug(f"User {user.id} has forgot their password: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, _: Optional[Request] = None
    ):
        logger.debug(f"Verification requested by user {user.id}: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users_backend = FastAPIUsers[User, UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users_backend.current_user(active=True)
current_super_user = fastapi_users_backend.current_user(active=True, superuser=True)
