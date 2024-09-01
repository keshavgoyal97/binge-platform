from pydantic import BaseModel, Field

from app.models.admin_type import AdminType


class AdminUser(BaseModel):
    user_id: str = Field(min_length=5, frozen=True)
    password: str = Field(min_length=5, frozen=True)
    admin_type: AdminType
