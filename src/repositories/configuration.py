from typing import Any, Sequence

from sqlalchemy import cast, desc, insert, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute

from models import Configuration


class ConfigurationRepository:
    model = Configuration

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, source_uuid: str, config_type: str, data: dict, name: str) -> Configuration:
        stmt = (
            insert(self.model)
            .values(source_uuid=source_uuid, config_type=config_type, data=data, name=name)
            .returning(self.model)
        )
        res = await self.db_session.execute(stmt)
        res = res.scalar_one()
        return res

    async def get_by_name(self, name: str, for_update: bool = False) -> Configuration | None:
        query = select(self.model).where(self.model.name == name)

        if for_update:
            query = query.with_for_update()

        res = await self.db_session.execute(query)
        return res.scalar_one_or_none()

    async def all(
        self,
        *args,
        per_page: int | None = None,
        page: int | None = None,
        for_update: bool = False,
        order_by: InstrumentedAttribute = None,
        desc_order: bool = False,
    ) -> Sequence[Any]:
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

    async def first(self, *args) -> Configuration:
        raw_result = await self.db_session.execute(select(self.model).filter(*args))
        result = raw_result.scalars().first()
        return result

    async def get_one_by_config_type_and_data(
        self, source_uuid: str, config_type: str, data: dict
    ) -> Configuration | None:
        query = select(self.model).filter(
            self.model.config_type == config_type,
            self.model.data == cast(data, JSONB),
            self.model.source_uuid == source_uuid,
        )

        res = await self.db_session.execute(query)
        res = res.scalar_one_or_none()

        return res

    async def get_list_by_config_type(self, config_type: str) -> list[Configuration]:
        query = select(self.model).filter(
            self.model.config_type == config_type,
        )

        res = await self.db_session.execute(query)
        configurations = res.scalars().all()
        return configurations
