from dataclasses import Field

from pydantic import BaseModel


class Slot(BaseModel):
    is_available: bool
    start_time: str = Field(min_length=5, max_length=5, frozen=True)
    end_time: str = Field(min_length=5, max_length=5, frozen=True)
    is_short_slot: bool
