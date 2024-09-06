from dataclasses import Field

from pydantic import BaseModel


class Slot(BaseModel):
    is_available: bool
    start_time: str
    end_time: str
    is_short_slot: bool
