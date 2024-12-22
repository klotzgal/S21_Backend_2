from fastapi import HTTPException
from models.address import Address
from schemas.client import ClientRequestSchema


async def create_client(client: ClientRequestSchema, uow):
    async with uow():
        if client.address_id is not None:
            address_id = await uow.address.first(Address.id == client.address_id)
            if address_id is None:
                raise HTTPException(status_code=404, detail="Address not found")
        
        client_id = await uow.client.create(**client.model_dump())

    return client_id