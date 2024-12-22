import uuid
from datetime import date

from sqlalchemy import UUID, Column, String, Date, ForeignKey

from db.session import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_name = Column(String(100), nullable=False)
    client_surname = Column(String(100), nullable=False)
    birthday = Column(Date(), nullable=False)
    gender = Column(String(100), nullable=False)
    registration_date = Column(Date(), nullable=False, default=date.today)
    address_id = Column(UUID(as_uuid=True), ForeignKey("address.id"), nullable=True)
