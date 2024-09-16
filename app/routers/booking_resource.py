from typing import List
from app.models.booking import Booking
from app.models.slot_availability_info import SlotAvailabilityInfo
from app.requests.confirm_booking import BookingConfirmation
from app.models.generic_response import GenericResponse
from app.requests.get_slots_request import GetSlotsRequest
from app.services.booking_service import BookingService
from app.utils.logger import logger
from fastapi import APIRouter
from datetime import datetime

_log = logger()

router = APIRouter(
    prefix='/v1/booking',
    tags=['booking']
)

booking_service = BookingService()


@router.post('/create')
def create_booking(request: Booking) -> GenericResponse:
    # Generate a timestamp-based ID
    timestamp_id = 'B' + datetime.now().strftime('%Y%m%d%H%M%S')
    request.id = timestamp_id

    return booking_service.create_booking(request=request)


@router.post('/confirm')
def confirm_booking(request: BookingConfirmation) -> GenericResponse:
    return booking_service.confirm_booking(request=request)


@router.post('/update')
def update_booking(request: Booking) -> GenericResponse:
    return booking_service.update_booking(request=request)


@router.put('/cancel')
def cancel_booking(existing_booking_id: str) -> GenericResponse:
    return booking_service.cancel_booking(booking_id=existing_booking_id)


@router.get('/get/phone_number/{phone_number}')
def get_bookings_from_phone_number(phone_number: str) -> List[Booking]:
    return booking_service.get_bookings_from_phone_number(phone_number=phone_number)


@router.get('/get/booking_id/{booking_id}')
def get_booking_from_booking_id(booking_id: str) -> Booking:
    return booking_service.get_booking_from_booking_id(booking_id=booking_id)


@router.get('/get/branch_id/{branch_id}/date/{date}')
def get_all_bookings(branch_id: str, date: str) -> List[Booking]:
    return booking_service.get_all_bookings(branch_id=branch_id, date=date)


@router.post('/get/slots')
def get_slots(request: GetSlotsRequest) -> List[SlotAvailabilityInfo]:
    return booking_service.get_slots(request=request)


@router.on_event("startup")
def send_booking_reminders():
    return booking_service.send_reminder()
