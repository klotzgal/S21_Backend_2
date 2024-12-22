from pydantic import BaseModel
from uuid import UUID


class BaseAddressSchema(BaseModel):
    country: str
    city: str
    street: str

class AddressSchema(BaseAddressSchema):
    id: UUID

