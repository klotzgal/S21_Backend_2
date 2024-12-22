
from pydantic import BaseModel


class Address(BaseModel):
    country: str
    city: str
    street: str