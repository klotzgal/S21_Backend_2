from fastapi import APIRouter

from api.v1.endpoints.health import health_router
from api.v1.endpoints.images import images_router
from api.v1.endpoints.products import product_router
from api.v1.endpoints.supplier import supplier_router
from api.v1.endpoints.client import client_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
api_router.include_router(images_router)
api_router.include_router(product_router)
api_router.include_router(supplier_router)
api_router.include_router(client_router)
