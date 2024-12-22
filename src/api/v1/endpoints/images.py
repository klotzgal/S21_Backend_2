from uuid import UUID
from fastapi import APIRouter, HTTPException, UploadFile
from api.dependencies import UOWDep
from models.images import Images
from schemas.errors import BaseErrorSchema
from schemas.images import ImageResponseSchema
from services.image import get_image_bytes

images_router = APIRouter(prefix="/images", tags=["images"])


@images_router.post(
    "/",
    status_code=200,
    responses={
        200: {"model": ImageResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def add_image(image: UploadFile, product_id: UUID, uow: UOWDep):
    async with uow():
        image_id = await uow.images.create(
            image=image.file.read(), product_id=product_id
        )

    return ImageResponseSchema(id=image_id)


@images_router.get(
    "/{image_id}",
    status_code=200,
    responses={
        200: {"content": {"application/octet-stream": {}}},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_image(image_id: UUID, uow: UOWDep):
    image = await get_image_bytes(image_id=image_id, uow=uow)

    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return str(image)


@images_router.put(
    "/{image_id}",
    status_code=200,
    responses={
        200: {"model": ImageResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def update_image(image_id: UUID, new_image: UploadFile, uow: UOWDep):
    async with uow():
        image = await uow.images.first(Images.id == image_id)

        if image is None:
            raise HTTPException(status_code=404, detail="Image not found")
        image.image = new_image.file.read()

    return ImageResponseSchema(id=image_id)


@images_router.delete(
    "/{image_id}",
    status_code=200,
    responses={
        200: {"model": {}},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def delete_image(image_id: UUID, uow: UOWDep):
    async with uow():
        if await uow.images.first(Images.id == image_id) is None:
            raise HTTPException(status_code=404, detail="Image not found")

        await uow.images.delete(Images.id == image_id)

    return {}


@images_router.get(
    "/product/{product_id}",
    status_code=200,
    responses={
        200: {"model": ImageResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_image_by_product_id(product_id: UUID, uow: UOWDep):
    async with uow():
        image = await uow.images.first(Images.product_id == product_id)

    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return str(image.image)
