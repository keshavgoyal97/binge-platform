from typing import List
from pydantic import BaseModel, Field

from app.models.slot import Slot


class SlotAvailabilityInfo(BaseModel):
    theatre_id: str = Field(min_length=3, frozen=True)
    number_of_slots_available: int = Field(ge=0)
    slots: List[Slot]
