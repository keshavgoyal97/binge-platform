from typing import List
from pydantic import BaseModel, Field


class About(BaseModel):
    header: str = Field(min_length=5, frozen=True)
    image: str = Field(min_length=5, frozen=True)
    paragraphs: List[str] = Field(min_length=1, frozen=True)
