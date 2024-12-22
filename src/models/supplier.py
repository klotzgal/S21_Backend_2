import uuid

from sqlalchemy import UUID, Column, String, ForeignKey

from db.session import Base


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    address_id = Column(UUID(as_uuid=True), ForeignKey("address.id"), nullable=True)
    phone_number = Column(String(100), nullable=True)
