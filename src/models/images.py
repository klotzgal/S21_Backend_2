import uuid

from sqlalchemy import UUID, Column, LargeBinary

from db.session import Base


class Images(Base):
    __tablename__ = "images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image = Column(LargeBinary(), nullable=False)
