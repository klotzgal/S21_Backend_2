from fastapi import HTTPException
from models.address import Address
from schemas.supplier import SupplierRequestSchema


async def create_supplier(supplier: SupplierRequestSchema, uow):
    async with uow():
        if supplier.address_id is not None:
            address_id = await uow.address.first(Address.id == supplier.address_id)
            if address_id is None:
                raise HTTPException(status_code=404, detail="Address not found")
        
        if supplier.phone_number is not None:
            if not supplier.phone_number.isdigit() or len(supplier.phone_number) > 11:
                raise HTTPException(status_code=400, detail="Invalid phone number")

        supplier_id = await uow.supplier.create(**supplier.model_dump())

    return supplier_id