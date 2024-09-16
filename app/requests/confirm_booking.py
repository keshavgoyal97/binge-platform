from pydantic import BaseModel, Field


class BookingConfirmation(BaseModel):
    payment_id: str = Field(min_length=5)
    order_id: str = Field(min_length=5)
    signature: str = Field(min_length=5)
