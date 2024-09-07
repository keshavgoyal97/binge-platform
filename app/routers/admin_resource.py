from fastapi import APIRouter

from app.models.admin_user import AdminUser
from app.requests.login_request import LoginRequest
from app.models.generic_response import GenericResponse
from app.models.login_response import LoginResponse
from app.services.admin_service import AdminService
from app.services.user_service import UserService
from app.utils.logger import logger

_log = logger()

router = APIRouter(
    prefix='/v1/admin',
    tags=['user']
)

admin_service = AdminService()
user_service = UserService()


@router.post("/login")
def admin_login(request: LoginRequest) -> LoginResponse:
    return admin_service.admin_login(request=request)


@router.post("/generate/bill")
def generate_bill(booking_id: str) -> GenericResponse:
    return admin_service.generate_bill(booking_id=booking_id)


@router.post("/create/user")
def create_user(new_user: AdminUser) -> GenericResponse:
    return admin_service.create_user(new_user=new_user)


@router.put("/delete/user")
def delete_user(user_id: str) -> GenericResponse:
    return admin_service.delete_user(user_id=user_id)


@router.post("/add/theatre")
def update_metadata_file(new_theatre_json: str) -> GenericResponse:
    return user_service.update_metadata_file(new_theatre_json=new_theatre_json)
