from fastapi import APIRouter

from app.models.admin_user import AdminUser
from app.models.theatre import Theatre
from app.requests.login_request import LoginRequest
from app.responses.generic_response import GenericResponse
from app.responses.login_response import LoginResponse
from app.utils.logger import logger

_log = logger()

router = APIRouter(
    prefix='/v1/admin',
    tags=['user']
)


@router.post("/login")
def admin_login(request: LoginRequest) -> LoginResponse:
    _log.info("No record found for phone number {}")
    pass


@router.post("/generate/bill")
def generate_bill(booking_id: str) -> GenericResponse:
    pass


@router.post("/create/user")
def create_user(new_user: AdminUser) -> GenericResponse:
    pass


@router.put("/delete/user")
def delete_user(user_id: str) -> GenericResponse:
    pass


@router.post("/add/theatre")
def add_theatre(new_theatre_json: str) -> GenericResponse:
    Theatre.model_validate_json(new_theatre_json)
    pass
