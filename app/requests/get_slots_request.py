from pydantic import BaseModel, Field
from datetime import date


class GetSlotsRequest(BaseModel):
    date: date
    branch_id: str = Field(min_length=5, max_length=5, frozen=True)
