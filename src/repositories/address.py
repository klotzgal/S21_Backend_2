from repositories.base import BaseRepository

from models import Address


class AddressRepository(BaseRepository):
    model = Address
