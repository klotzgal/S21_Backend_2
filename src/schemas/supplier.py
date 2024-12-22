from uuid import UUID
from pydantic import BaseModel

from schemas.address import AddressSchema


class SupplierRequestSchema(BaseModel):
    name: str
    address: AddressSchema | None = None
    phone_number: str | None = None

class SupplierResponseSchema(BaseModel):
    id: UUID

class SupplerFullResponseSchema(SupplierRequestSchema, SupplierResponseSchema):
    pass

class SupplierChangeAddressSchema(BaseModel):
    address: AddressSchema
