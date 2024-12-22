import asyncio

import pytest
from httpx import AsyncClient

from api.dependencies import UnitOfWork
from app.app import create_app
from db.session import Base, engine


@pytest.fixture(scope="function", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    app = create_app()
    # здесь можно переопределить зависимости на тестовые
    # app.dependency_overrides[SomeAdapter] = SomeMockAdapter
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def uow() -> UnitOfWork:
    uow = UnitOfWork()
    yield uow
