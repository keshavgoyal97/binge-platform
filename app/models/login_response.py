from pydantic import BaseModel

from app.models.admin_type import AdminType


class LoginResponse(BaseModel):
    success: bool
    error_message: str
    admin_type: AdminType
