from fastapi import APIRouter

from api.v1.endpoints.health import health_router

api_router = APIRouter()
api_router.include_router(health_router)
