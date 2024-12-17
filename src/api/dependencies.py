from abc import ABC, abstractmethod
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_database_session_maker
from repositories import ConfigurationRepository


class IUnitOfWork(ABC):
    configuration: ConfigurationRepository | None
    db_session: AsyncSession

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...


class UnitOfWork:
    configuration: ConfigurationRepository | None

    def __init__(self):
        self.database_session_factory = async_database_session_maker
        self.auto_commit: bool = True
        self.db_session = None

    def __call__(self):
        return self

    async def __aenter__(self):
        self.db_session = self.database_session_factory()
        self.configuration = ConfigurationRepository(self.db_session)

    async def __aexit__(self, exc_type, exc, tb):
        if self.db_session is not None:
            if exc_type is not None:
                await self.rollback()
            if self.auto_commit:
                await self.commit()

            await self.db_session.close()

    async def commit(self):
        await self.db_session.commit()

    async def rollback(self):
        await self.db_session.rollback()


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
