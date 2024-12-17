from fastapi import APIRouter

health_router = APIRouter()


@health_router.get('/health', tags=['health'])
async def health_check():
    return "I'm alive"
