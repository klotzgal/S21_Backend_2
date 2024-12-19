from repositories.base import BaseRepository

from models import Images


class ImagesRepository(BaseRepository):
    model = Images
