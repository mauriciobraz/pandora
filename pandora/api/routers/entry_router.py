from fastapi import status, APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse

entry_router = APIRouter()


@entry_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_class=JSONResponse,
    responses={
        status.HTTP_200_OK: {
            "model": str,
            "content": {
                "application/json": {"example": {"message": "Hello World!"}},
            },
        }
    },
)
async def get_root():
    return JSONResponse(
        {"message": "Hello World!"},
        status_code=status.HTTP_200_OK,
    )


@entry_router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    response_class=PlainTextResponse,
    responses={
        status.HTTP_200_OK: {
            "model": str,
            "content": {
                "text/plain": {"example": "OK"},
            },
        }
    },
)
async def get_health():
    return "OK"


@entry_router.get(
    "/status",
    status_code=status.HTTP_200_OK,
    response_class=JSONResponse,
)
async def get_status():
    return JSONResponse(
        {
            "api": "OK",
            "cache": "OK",
            "database": "OK",
        },
        status_code=status.HTTP_200_OK,
    )
