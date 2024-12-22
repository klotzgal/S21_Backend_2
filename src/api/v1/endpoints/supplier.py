from uuid import UUID
from fastapi import APIRouter, HTTPException
from api.dependencies import UOWDep
from models.address import Address
from models.supplier import Supplier
from schemas.errors import BaseErrorSchema
from schemas.supplier import SupplerFullResponseSchema, SupplierChangeAddressSchema, SupplierRequestSchema, SupplierResponseSchema
from services.suppler import create_supplier
from schemas.address import AddressSchema

supplier_router = APIRouter(prefix="/suppliers", tags=["suppliers"])


@supplier_router.post(
    "/",
    status_code=200,
    responses={
        200: {"model": SupplierResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def add_supplier(supplier: SupplierRequestSchema, uow: UOWDep):
    supplier_id = await create_supplier(supplier, uow)
    return SupplierResponseSchema(id=supplier_id)


@supplier_router.patch(
    "/{supplier_id}",
    status_code=200,
    responses={
        200: {"model": SupplerFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def update_supplier(
    supplier_id: UUID, data: SupplierChangeAddressSchema, uow: UOWDep
):
    async with uow():
        supplier = await uow.supplier.first(Supplier.id == supplier_id)
        if supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")

        address_id = await uow.address.create(**data.address.model_dump())
        supplier.address_id = address_id
        address = await uow.address.first(Address.id == supplier.address_id)
        address = AddressSchema(
            id=address.id,
            country=address.country,
            city=address.city,
            street=address.street,
        )

    return SupplerFullResponseSchema(
        id=supplier.id,
        name=supplier.name,
        address=address,
        phone_number=supplier.phone_number,
    )


@supplier_router.get(
    "/{supplier_id}",
    status_code=200,
    responses={
        200: {"model": SupplerFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_supplier(supplier_id: UUID, uow: UOWDep):
    async with uow():
        supplier = await uow.supplier.first(Supplier.id == supplier_id)

        if supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")
        address = await uow.address.first(Address.id == supplier.address_id)

        if address is not None:
            address = AddressSchema(
            id=address.id,
            country=address.country,
            city=address.city,
            street=address.street,
        )
            
    return SupplerFullResponseSchema(
        id=supplier.id,
        name=supplier.name,
        address=address,
        phone_number=supplier.phone_number,
    )


@supplier_router.get(
    "/",
    status_code=200,
    responses={
        200: {"model": list[SupplerFullResponseSchema]},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_all_supplier(uow: UOWDep):
    async with uow():
        suppliers = await uow.supplier.all()
        
        for supplier in suppliers:
            address = await uow.address.first(Address.id == supplier.address_id)

            if address is not None:
                address = AddressSchema(
                id=address.id,
                country=address.country,
                city=address.city,
                street=address.street,
            )
            supplier.address = address
        

    return [
        SupplerFullResponseSchema(
            id=supplier.id,
            name=supplier.name,
            address=supplier.address,
            phone_number=supplier.phone_number,
        )
        for supplier in suppliers
    ]


@supplier_router.delete(
    "/{supplier_id}",
    status_code=200,
    responses={
        200: {"model": {}},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def delete_supplier(supplier_id: UUID, uow: UOWDep):
    async with uow():
        if await uow.supplier.first(Supplier.id == supplier_id) is None:
            raise HTTPException(status_code=404, detail="Supplier not found")

        await uow.supplier.delete(Supplier.id == supplier_id)
    return {}

