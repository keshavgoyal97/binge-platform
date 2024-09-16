from datetime import datetime

from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    otp: str = Field(min_length=1, max_length=10, frozen=True)
    phone_number: str = Field(min_length=10, max_length=10, frozen=True)
    created_at: datetime.datetime
