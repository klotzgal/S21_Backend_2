from uuid import UUID
from fastapi import APIRouter, HTTPException
from api.dependencies import UOWDep
from models.product import Product
from schemas.errors import BaseErrorSchema
from schemas.product import (
    ProductDecreaseAvailableStockSchema,
    ProductFullResponseSchema,
    ProductRequestSchema,
    ProductResponseSchema,
)

product_router = APIRouter(prefix="/products", tags=["products"])


@product_router.post(
    "/",
    status_code=200,
    responses={
        200: {"model": ProductResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def add_product(product: ProductRequestSchema, uow: UOWDep):
    async with uow():
        product_id = await uow.product.create(**product.model_dump())
    return ProductResponseSchema(id=product_id)


@product_router.patch(
    "/{product_id}",
    status_code=200,
    responses={
        200: {"model": ProductFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def update_product(
    product_id: UUID, data: ProductDecreaseAvailableStockSchema, uow: UOWDep
):
    async with uow():
        product = await uow.product.first(Product.id == product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")

        product.available_stock -= data.count
        if product.available_stock < 0:
            raise HTTPException(status_code=409, detail="Not enough stock")

    return ProductFullResponseSchema(
        id=product.id,
        name=product.name,
        category=product.category,
        price=product.price,
        available_stock=product.available_stock,
        last_update_date=product.last_update_date,
        supplier_id=product.supplier_id,
        image_id=product.image_id,
    )


@product_router.get(
    "/{product_id}",
    status_code=200,
    responses={
        200: {"model": ProductFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_product(product_id: UUID, uow: UOWDep):
    async with uow():
        product = await uow.product.first(Product.id == product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductFullResponseSchema(
        id=product.id,
        name=product.name,
        category=product.category,
        price=product.price,
        available_stock=product.available_stock,
        last_update_date=product.last_update_date,
        supplier_id=product.supplier_id,
        image_id=product.image_id,
    )


@product_router.get(
    "/",
    status_code=200,
    responses={
        200: {"model": list[ProductFullResponseSchema]},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_all_product(uow: UOWDep):
    async with uow():
        products = await uow.product.all()

    return [
        ProductFullResponseSchema(
            id=product.id,
            name=product.name,
            category=product.category,
            price=product.price,
            available_stock=product.available_stock,
            last_update_date=product.last_update_date,
            supplier_id=product.supplier_id,
            image_id=product.image_id,
        )
        for product in products
    ]


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
