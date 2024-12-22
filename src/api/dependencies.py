from abc import ABC, abstractmethod
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_database_session_maker
from repositories import (
    AddressRepository,
    ClientRepository,
    ImagesRepository,
    ProductRepository,
    SupplierRepository,
)


class IUnitOfWork(ABC):
    address: AddressRepository | None
    client: ClientRepository | None
    images: ImagesRepository | None
    product: ProductRepository | None
    supplier: SupplierRepository | None
    db_session: AsyncSession

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...


class UnitOfWork:
    address: AddressRepository | None
    client: ClientRepository | None
    images: ImagesRepository | None
    product: ProductRepository | None
    supplier: SupplierRepository | None

    def __init__(self):
        self.database_session_factory = async_database_session_maker
        self.auto_commit: bool = True
        self.db_session = None

    def __call__(self):
        return self

    async def __aenter__(self):
        self.db_session = self.database_session_factory()
        self.address = AddressRepository(self.db_session)
        self.client = ClientRepository(self.db_session)
        self.images = ImagesRepository(self.db_session)
        self.product = ProductRepository(self.db_session)
        self.supplier = SupplierRepository(self.db_session)

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
