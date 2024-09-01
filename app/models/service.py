from pydantic import BaseModel, Field


class Service(BaseModel):
    id: str = Field(min_length=5, max_length=5, frozen=True)
    name: str = Field(min_length=5, frozen=True)
    image: str = Field(min_length=5, frozen=True)
