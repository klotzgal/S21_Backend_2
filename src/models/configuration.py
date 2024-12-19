import uuid

from sqlalchemy import UUID, Column, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB

from db.session import Base
from utils.common import get_current_time_with_tz


class Configuration(Base):
    __tablename__ = 'configuration'

    name = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    source_uuid = Column(UUID(as_uuid=True), nullable=False)
    config_type = Column(String(255), nullable=False)
    data = Column(JSONB(), nullable=False)
    created_at = Column(DateTime(timezone=True), default=get_current_time_with_tz, nullable=False)
