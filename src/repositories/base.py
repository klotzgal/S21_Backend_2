import uuid
from abc import ABC, abstractmethod
from typing import Type, Sequence

from sqlalchemy import insert, select, update, desc, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql.functions import count


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError


class BaseRepository(AbstractRepository):
    model = None

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, **kwargs):
        stmt = insert(self.model).values(**kwargs).returning(self.model.id)
        res = await self.db_session.execute(stmt)
        return res.scalar_one()

    async def get_one(self, **kwargs) -> uuid.UUID | None:
        query = select(self.model.id).filter_by(**kwargs)
        res = await self.db_session.execute(query)
        return res.scalars().first()

    async def first(
        self, *args, order_by: InstrumentedAttribute = None, for_update: bool = False
    ) -> Type[model]:
        query = select(self.model).where(*args)

        if order_by is not None:
            query = query.order_by(order_by)

        if for_update:
            query = query.with_for_update()

        raw_result = await self.db_session.execute(query)
        result = raw_result.scalars().first()
        return result

    async def all(
        self,
        *args,
        per_page: int | None = None,
        page: int | None = None,
        for_update: bool = False,
        order_by: InstrumentedAttribute = None,
        desc_order: bool = False,
    ) -> Sequence[Type[model]]:
        query = select(self.model).where(*args)

        if per_page is not None:
            query = query.limit(per_page)

        if page is not None:
            query = query.offset((page - 1) * per_page)

        if for_update:
            query = query.with_for_update()

        if order_by is not None:
            if desc_order:
                query = query.order_by(desc(order_by))
            else:
                query = query.order_by(order_by)

        raw_result = await self.db_session.execute(query)

        result = raw_result.scalars().all()

        return result

    async def update(self, filter_by: list, values: dict):
        stmt = update(self.model).where(*filter_by).values(**values)
        await self.db_session.execute(stmt)

    async def count(self, *args) -> int:
        query = select(count(self.model.id)).where(*args)

        raw_result = await self.db_session.execute(query)

        return raw_result.scalar()

    async def delete(self, *args) -> int:
        query = delete(self.model).where(*args)

        raw_result = await self.db_session.execute(query)

        return raw_result.rowcount
