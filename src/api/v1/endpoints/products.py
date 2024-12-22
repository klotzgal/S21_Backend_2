from uuid import UUID
from fastapi import APIRouter, HTTPException
from api.dependencies import UOWDep
from models.product import Product
from schemas.errors import BaseErrorSchema
from schemas.product import ProductSchema

product_router = APIRouter(prefix="/product", tags=["product"])


@product_router.post(
    "/",
    status_code=200,
    responses={
        200: {"model": ProductSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def add_product(product: ProductSchema, uow: UOWDep):
    async with uow():
        product_id = await uow.product.create(product.model_dump())
    return ProductSchema(product_id=product_id)


# Уменьшение количества товара (на вход запросу подается id товара и на сколько уменьшить)


@product_router.put(
    "/{product_id}",
    status_code=200,
    responses={
        200: {"model": ProductSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def update_product(product_id: UUID, product: Product, uow: UOWDep):
    async with uow():
        product = await uow.product.first(Product.id == product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        await uow.product.update(Product.id == product_id, values=product.dict())
    return ProductSchema(product_id=product_id)


# Получение товара по id


@product_router.get(
    "/{product_id}",
    status_code=200,
    responses={
        200: {"model": ProductSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_product(product_id: UUID, uow: UOWDep):
    async with uow():
        product = await uow.product.first(Product.id == product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Получение всех доступных товаров


@product_router.get(
    "/",
    status_code=200,
    responses={
        200: {"model": list[ProductSchema]},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_all_product(uow: UOWDep):
    async with uow():
        product = await uow.product.all()
    return product


# Удаление товара по id


@product_router.delete(
    "/{product_id}",
    status_code=200,
    responses={
        200: {"model": {}},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def delete_product(product_id: UUID, uow: UOWDep):
    async with uow():
        if await uow.product.first(Product.id == product_id) is None:
            raise HTTPException(status_code=404, detail="Product not found")
        await uow.product.delete(Product.id == product_id)
    return {}
