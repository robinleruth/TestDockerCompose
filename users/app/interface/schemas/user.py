from typing import List

from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    password: str
    scopes: List[str]
