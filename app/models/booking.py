import datetime
from datetime import date
from pydantic import BaseModel, Field

from app.models.booking_status import BookingStatus
from app.models.user_type import UserType


class Booking(BaseModel):
    id: str = Field(min_length=13, max_length=13)
    created_by: UserType
    admin_name: str = Field(min_length=3, frozen=True)
    created_at: datetime.datetime
    last_updated_at: datetime.datetime
    status: BookingStatus
    booking_name: str = Field(min_length=3, frozen=True)
    booking_date: date
    start_time: str = Field(min_length=5, max_length=5, frozen=True)
    end_time: str = Field(min_length=5, max_length=5, frozen=True)
    theatre_id: str = Field(min_length=5, max_length=5, frozen=True)
    branch_id: str = Field(min_length=5, max_length=5, frozen=True)
    email: str = Field(min_length=5, max_length=100, frozen=True)
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
