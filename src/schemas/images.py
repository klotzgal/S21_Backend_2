from typing import Any
from uuid import UUID

from pydantic import BaseModel


class ImageRequestSchema(BaseModel):
    data: dict[str, Any]


class ImageResponseSchema(BaseModel):
    id: UUID
