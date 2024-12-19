from typing import Any

from pydantic import BaseModel



class CreateConfigInSchema(BaseModel):
    data: dict[str, Any]
