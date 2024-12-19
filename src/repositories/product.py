from repositories.base import BaseRepository

from models import Product


class ProductRepository(BaseRepository):
    model = Product
