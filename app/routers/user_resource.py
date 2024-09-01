from typing import List

from app.models.all_info import AllInfo
from app.models.slot_availability_info import SlotAvailabilityInfo
from app.requests.get_slots_request import GetSlotsRequest
from app.responses.generic_response import GenericResponse
from app.utils.logger import logger
from fastapi import APIRouter

_log = logger()

router = APIRouter(
    prefix='/v1/user',
    tags=['user']
)


@router.post("/send/otp")
def send_otp(phone_number: str) -> GenericResponse:
    _log.info("No record found for phone number {}".format(phone_number))
    pass


@router.post("/validate/otp")
def validate_otp(phone_number: str, otp: str) -> GenericResponse:
    pass


@router.get('/get/all/info')
def get_all_info() -> AllInfo:
    pass


@router.post('/get/slots')
def get_slots(request: GetSlotsRequest) -> List[SlotAvailabilityInfo]:
    pass
