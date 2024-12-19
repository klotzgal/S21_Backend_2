from repositories.base import BaseRepository

from models import Supplier


class SupplierRepository(BaseRepository):
    model = Supplier
