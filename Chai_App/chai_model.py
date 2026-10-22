from pydantic import BaseModel


class Chai(BaseModel):
    id: int
    name: str
    categories: list

