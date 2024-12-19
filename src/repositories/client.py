from repositories.base import BaseRepository

from models import Client


class ClientRepository(BaseRepository):
    model = Client
