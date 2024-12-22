from datetime import date
from uuid import UUID
from pydantic import BaseModel, Field


class ProductRequestSchema(BaseModel):
    name: str
    category: str
    price: int = Field(ge=0, default=0)
    available_stock: int = Field(ge=0, default=0)
    last_update_date: date = date.today()
    supplier_id: UUID
    image_id: UUID | None = None


class ProductResponseSchema(BaseModel):
    id: UUID


class ProductFullResponseSchema(ProductRequestSchema, ProductResponseSchema):
    pass


class ProductDecreaseAvailableStockSchema(BaseModel):
    count: int = Field(ge=0, default=0)
