from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.api import api_router
from utils.setup_logging import setup_logging

setup_logging()


@asynccontextmanager
async def lifespan(fastapi: FastAPI):
    yield


app = FastAPI(
    title="Shop API",
    version="1.0",
    openapi_url="/swagger/openapi.json",
    docs_url="/swagger",
    lifespan=lifespan,
)

app.include_router(api_router)
