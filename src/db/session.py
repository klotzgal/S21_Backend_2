from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from core.config import settings

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    pool_size=50,
)
async_database_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_database_session_maker() as session:
        yield session

convention = {
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
}

Base = declarative_base(metadata=MetaData(naming_convention=convention))
Base.metadata.schema = settings.POSTGRES_SCHEMA
