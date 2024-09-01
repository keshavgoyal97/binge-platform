from typing import List
from app.models.booking import Booking
from app.requests.confirm_booking import BookingConfirmation
from app.responses.generic_response import GenericResponse
from app.utils.logger import logger
from fastapi import APIRouter
from datetime import datetime

_log = logger()

router = APIRouter(
    prefix='/v1/booking',
    tags=['booking']
)


@router.post('/create')
def create_booking(request: Booking) -> GenericResponse:
    # Generate a timestamp-based ID
    timestamp_id = 'B' + datetime.now().strftime('%Y%m%d%H%M%S')
    pass


@router.post('/confirm')
def confirm_booking(request: BookingConfirmation) -> GenericResponse:
    pass


@router.post('/update')
def update_booking(request: Booking) -> GenericResponse:
    pass


@router.put('/cancel')
def cancel_booking(existing_booking_id: str) -> GenericResponse:
    pass


@router.get('/get/phone_number/{phone_number}')
def get_bookings_from_phone_number(phone_number: str) -> List[Booking]:
    _log.info("No record found for phone number {}".format(phone_number))

    pass


@router.get('/get/booking_id/{booking_id}')
def get_booking_from_booking_id(booking_id: str) -> Booking:
    _log.info("No record found for booking_id {}".format(booking_id))

    pass


@router.get('/get/branch_id/{branch_id}/date/{date}')
def get_all_bookings(branch_id: str, date: str) -> List[Booking]:
    pass
