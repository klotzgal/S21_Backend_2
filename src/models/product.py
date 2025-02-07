import uuid

from sqlalchemy import UUID, Column, Date, String, Integer, ForeignKey

from db.session import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    available_stock = Column(Integer, nullable=False)
    last_update_date = Column(Date(), nullable=False)
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("supplier.id"), nullable=False)
    image_id = Column(UUID(as_uuid=True), ForeignKey("images.id", ondelete="CASCADE"), nullable=True)
