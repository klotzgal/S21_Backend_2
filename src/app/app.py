from contextlib import asynccontextmanager

from fastapi import FastAPI

from utils.setup_logging import setup_logging
from api.v1.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title="Shop API",
        version="1.0",
        openapi_url="/swagger/openapi.json",
        docs_url="/swagger",
        lifespan=lifespan,
    )

    app.include_router(api_router)

    return app
