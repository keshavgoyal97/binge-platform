from pydantic import BaseModel, Field


class Slot(BaseModel):
    is_available: bool = True
    start_time: str = Field(min_length=5, max_length=5, frozen=True)
    end_time: str = Field(min_length=5, max_length=5, frozen=True)
    is_short_slot: bool = False
