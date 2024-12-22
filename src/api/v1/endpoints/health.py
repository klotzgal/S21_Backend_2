from fastapi import APIRouter

health_router = APIRouter(prefix="/health")


@health_router.get("/", tags=["health"])
async def health_check():
    return "I'm alive"
