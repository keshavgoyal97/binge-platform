from app.exceptions.validation_exceptions import (
    EmptyPhoneNumbersListException,
    ExceedPhoneNumbersListLengthException,
    InvalidPhoneNumberException,
)
from pydantic import BaseModel, validator, Field
from datetime import date


class GetSlotsRequest(BaseModel):
    date: date
    branch_id: str = Field(min_length=3, frozen=True)
