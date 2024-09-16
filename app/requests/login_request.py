from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    user_id: str = Field(min_length=5)
    password: str = Field(min_length=5)
