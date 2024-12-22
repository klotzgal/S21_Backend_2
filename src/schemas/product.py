from datetime import date
from uuid import UUID
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: UUID
    name: str
    category: str
    price: int
    available_stock: int
    last_update_date: date = date.today()
    supplier_id: UUID | None = None
    image_id: UUID | None = None
