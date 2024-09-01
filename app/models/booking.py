import datetime
from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr, Field

from app.models.booking_status import BookingStatus
from app.models.user_type import UserType


class Booking(BaseModel):
    created_by: UserType
    admin_name: str = Field(min_length=3, frozen=True)
    created_at: datetime.datetime
    status: BookingStatus
    booking_name: str = Field(min_length=3, frozen=True)
    booking_date: date
    start_time: str = Field(min_length=5, max_length=5, frozen=True)
    end_time: str = Field(min_length=5, max_length=5, frozen=True)
    theatre_id: str = Field(min_length=5, max_length=5, frozen=True)
    email: EmailStr
    phone_number: str = Field(min_length=10, max_length=10, frozen=True)
    total_price: int = Field(ge=100, frozen=True)
    advance_paid: int = Field(ge=100, frozen=True)
    number_of_people: int = Field(ge=1, frozen=True)
    decor_type: str = Field(min_length=3, frozen=True)
    decor_name_1: str = Field(min_length=5, frozen=True)
    decor_name_2: str
    add_on_ids: str
    cake_ids: str
    duration: int = Field(ge=2, frozen=True)
