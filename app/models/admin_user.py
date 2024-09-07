from datetime import datetime

from pydantic import BaseModel, Field

from app.models.admin_type import AdminType


class AdminUser(BaseModel):
    user_id: str = Field(min_length=5, frozen=True)
    password: str = Field(min_length=5, frozen=True)
    phone_number: str = Field(min_length=10, max_length=10, frozen=True)
    email: str = Field(min_length=5, max_length=100, frozen=True)
    admin_type: AdminType
    created_at: datetime.datetime
