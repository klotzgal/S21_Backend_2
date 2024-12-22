import uuid

from sqlalchemy import UUID, Column, String

from db.session import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    street = Column(String(100), nullable=False)
