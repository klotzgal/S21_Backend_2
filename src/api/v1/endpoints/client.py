from uuid import UUID
from fastapi import APIRouter, HTTPException
from api.dependencies import UOWDep
from models.address import Address
from models.client import Client
from schemas.errors import BaseErrorSchema
from schemas.client import ClientChangeAddressSchema, ClientFullResponseSchema, ClientRequestSchema, ClientResponseSchema
from schemas.address import AddressSchema
from services.client import create_client

client_router = APIRouter(prefix="/clients", tags=["clients"])

@client_router.post(
    "/",
    status_code=200,
    responses={
        200: {"model": ClientResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def add_client(client: ClientRequestSchema, uow: UOWDep):
    client_id = await create_client(client, uow)

    return ClientResponseSchema(id=client_id)

@client_router.patch(
    "/{client_id}",
    status_code=200,
    responses={
        200: {"model": ClientFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def update_client(
    client_id: UUID, data: ClientChangeAddressSchema, uow: UOWDep
):
    async with uow():
        client = await uow.client.first(Client.id == client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")

        address_id = await uow.address.create(**data.address.model_dump())
        client.address_id = address_id
        address = await uow.address.first(Address.id == client.address_id)
        address = AddressSchema(
            id=address.id,
            country=address.country,
            city=address.city,
            street=address.street,
        )
        

    return ClientFullResponseSchema(
            id=client.id,
            client_name=client.client_name,
            client_surname=client.client_surname,
            address=address,
            birthday=client.birthday,
            gender=client.gender,
            registration_date=client.registration_date
        )

@client_router.get(
    "/{client_id}",
    status_code=200,
    responses={
        200: {"model": ClientFullResponseSchema},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_client(client_id: UUID, uow: UOWDep):
    async with uow():
        client = await uow.client.first(Client.id == client_id)

        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")

        address = await uow.address.first(Address.id == client.address_id)

        if address is not None:
            address = AddressSchema(
            id=address.id,
            country=address.country,
            city=address.city,
            street=address.street,
        )
            
    return ClientFullResponseSchema(
            id=client.id,
            client_name=client.client_name,
            client_surname=client.client_surname,
            address=address,
            birthday=client.birthday,
            gender=client.gender,
            registration_date=client.registration_date
        )

@client_router.get(
    "/",
    status_code=200,
    responses={
        200: {"model": list[ClientFullResponseSchema]},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def get_all_client(uow: UOWDep):
    async with uow():
        clients = await uow.client.all()
        
        for client in clients:
            address = await uow.address.first(Address.id == client.address_id)

            if address is not None:
                address = AddressSchema(
                id=address.id,
                country=address.country,
                city=address.city,
                street=address.street,
            )
            client.address = address


    return [
        ClientFullResponseSchema(
            id=client.id,
            client_name=client.client_name,
            client_surname=client.client_surname,
            address=client.address,
            birthday=client.birthday,
            gender=client.gender,
            registration_date=client.registration_date
        )
        for client in clients
    ]

@client_router.delete(
    "/{client_id}",
    status_code=200,
    responses={
        200: {"model": {}},
        400: {"model": BaseErrorSchema},
        404: {"model": BaseErrorSchema},
    },
)
async def delete_client(client_id: UUID, uow: UOWDep):
    async with uow():
        if await uow.client.first(Client.id == client_id) is None:
            raise HTTPException(status_code=404, detail="Client not found")

        await uow.client.delete(Client.id == client_id)
    return {}

