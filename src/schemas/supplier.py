from uuid import UUID
from pydantic import BaseModel

from schemas.address import Address


class SupplierRequestSchema(BaseModel):
    name: str
    address: Address | None = None
    phone_number: str | None = None

class SupplierResponseSchema(BaseModel):
    id: UUID

class SupplerFullResponseSchema(SupplierRequestSchema, SupplierResponseSchema):
    pass

class SupplierChangeAddressSchema(BaseModel):
    address: Address
