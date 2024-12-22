from datetime import date
from uuid import UUID
from pydantic import BaseModel

from schemas.address import AddressSchema


class ClientRequestSchema(BaseModel):
    client_name: str
    client_surname: str
    birthday: date
    gender: str
    registration_date: date = date.today()
    address: AddressSchema | None = None


class ClientResponseSchema(BaseModel):
    id: UUID

class ClientFullResponseSchema(ClientRequestSchema, ClientResponseSchema):
    pass

class ClientChangeAddressSchema(BaseModel):
    address: AddressSchema
