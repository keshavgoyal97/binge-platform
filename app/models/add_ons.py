from pydantic import BaseModel, Field


class AddOns(BaseModel):
    id: str = Field(min_length=3, frozen=True)
    name: str = Field(min_length=3, frozen=True)
    price: int = Field(ge=100, frozen=True)
    image: str = Field(min_length=5, frozen=True)
