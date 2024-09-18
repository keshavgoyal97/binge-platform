from typing import List
from pydantic import BaseModel, Field

from app.models.slot import Slot


class Theatre(BaseModel):
    id: str = Field(min_length=5, max_length=5, frozen=True)
    name: str = Field(min_length=5, frozen=True)
    city: str = Field(min_length=5, frozen=True)
    branch_id: str = Field(min_length=5, max_length=5, frozen=True)
    gallery_photos: List[str] = Field(min_length=1, frozen=True)
    gallery_video: str = Field(min_length=5, frozen=True)
    all_slots: List[Slot] = Field(min_length=3, max_length=6, frozen=True)
