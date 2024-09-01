from pydantic import BaseModel

from app.models.admin_type import AdminType


class GenericResponse(BaseModel):
    success: bool
    error_code: int
    error_message: str
