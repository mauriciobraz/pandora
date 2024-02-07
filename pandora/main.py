import uvicorn

from dotenv import load_dotenv
from loguru import logger

from fastapi import FastAPI
from pydantic import ValidationError

from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from .api.errors.exception_handlers import (
    DataException,
    ServiceException,
    ExceptionHandlers,
)

from .api.routers.auth_router import auth_router
from .api.routers.entry_router import entry_router
from .api.routers.query_router import query_router
from .api.routers.document_router import document_router

from .helpers.dotenv import get_env_variable

logger.add(
    sink="logs/logs.log",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
    rotation="1 week",
    backtrace=True,
    diagnose=True,
)

load_dotenv()


def main() -> FastAPI:
    app = FastAPI(
        tile="Pandora",
        description="A privacy-focused RAG bot.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(
        DataException,
        ExceptionHandlers.data_exception,  # type: ignore
    )

    app.add_exception_handler(
        HTTPException,
        ExceptionHandlers.http_exception,  # type: ignore
    )

    app.add_exception_handler(
        ServiceException,
        ExceptionHandlers.service_exception,  # type: ignore
    )

    app.add_exception_handler(
        ValidationError,
        ExceptionHandlers.validation_exception,
    )

    app.add_exception_handler(
        Exception,
        ExceptionHandlers.unhandled_exception,
    )

    app.include_router(auth_router)
    app.include_router(entry_router)

    app.include_router(query_router)
    app.include_router(document_router)

    return app


def start() -> None:
    uvicorn.run(
        app=main(),
        port=get_env_variable(int, "PORT", 8000),
        host=get_env_variable(str, "HOST", "0.0.0.0"),
    )
