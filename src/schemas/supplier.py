from uuid import UUID
from pydantic import BaseModel

from schemas.address import AddressSchema, BaseAddressSchema


class SupplierRequestSchema(BaseModel):
    name: str
    address_id: UUID | None = None
    phone_number: str | None = None

class SupplierResponseSchema(BaseModel):
    id: UUID

class SupplerFullResponseSchema( SupplierResponseSchema):
    name: str
    address: AddressSchema | None = None
    phone_number: str | None = None

class SupplierChangeAddressSchema(BaseModel):
    address: BaseAddressSchema
