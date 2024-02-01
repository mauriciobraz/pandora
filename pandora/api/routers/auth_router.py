from fastapi import APIRouter

from ...helpers.users import fastapi_users_backend, auth_backend
from ...schemas.user_schemas import UserRead, UserCreate, UserUpdate

auth_router = APIRouter(
    prefix="/auth",
)

auth_router.include_router(
    prefix="/jwt",
    router=fastapi_users_backend.get_auth_router(auth_backend),
)

internal_routers = [
    fastapi_users_backend.get_reset_password_router(),
    fastapi_users_backend.get_verify_router(UserRead),
    fastapi_users_backend.get_register_router(UserRead, UserCreate),
]

for router in internal_routers:
    auth_router.include_router(router)
