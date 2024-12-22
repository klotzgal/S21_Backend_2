from pydantic import BaseModel


class BaseErrorSchema(BaseModel):
    detail: str
