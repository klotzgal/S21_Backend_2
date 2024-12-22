from uuid import UUID

from models import Images


async def get_image_bytes(image_id: UUID, uow):
    async with uow():
        image = await uow.images.first(Images.id == image_id)

    if image is None:
        return None
    return image.image
