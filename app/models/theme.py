from pydantic import BaseModel, Field


class About(BaseModel):
    id: str = Field(min_length=5, max_length=5, frozen=True)
    name: str = Field(min_length=5, frozen=True)
    image: str = Field(min_length=5, frozen=True)
    single_person_celebration: bool
