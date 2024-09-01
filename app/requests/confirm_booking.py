from app.exceptions.validation_exceptions import (
    InvalidPhoneNumberException, MissingRequiredField,
)
from pydantic import BaseModel, validator, Field


class BookingConfirmation(BaseModel):
    payment_id: str = Field(min_length=5)
    order_id: str = Field(min_length=5)
    signature: str = Field(min_length=5)
