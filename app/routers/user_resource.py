from app.models.all_info import AllInfo
from app.models.generic_response import GenericResponse
from app.services.user_service import UserService
from app.utils.logger import logger
from fastapi import APIRouter

_log = logger()

router = APIRouter(
    prefix='/v1/user',
    tags=['user']
)

user_service = UserService()


@router.post("/send/otp")
def send_otp(phone_number: str) -> GenericResponse:
    return user_service.send_otp_through_sms(phone_number=phone_number)


@router.post("/validate/otp")
def validate_otp(phone_number: str, otp: str) -> GenericResponse:
    return user_service.validate_otp(phone_number=phone_number, otp=otp)


@router.get('/get/all/info')
def get_all_info() -> AllInfo:
    return user_service.get_all_info()
