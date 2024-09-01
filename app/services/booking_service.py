from typing import List
from app.models.all_info import AllInfo
from app.models.booking import Booking
from app.models.slot_availability_info import SlotAvailabilityInfo
from app.requests.confirm_booking import BookingConfirmation
from app.requests.create_booking import CreateBooking
from app.requests.get_slots_request import GetSlotsRequest
from app.responses.generic_response import GenericResponse
from app.utils.logger import logger
from uuid import UUID, uuid1

from datetime import datetime

_log = logger()


class BookingService:

    def get_all_info(self) -> AllInfo:
        _log.info("No record found for phone number {}".format(phone_number))

        pass

    def get_slots(self, request: GetSlotsRequest) -> List[SlotAvailabilityInfo]:
        pass

    def create_booking(self, request: CreateBooking) -> GenericResponse:
        # Generate a timestamp-based ID
        timestamp_id = 'B' + datetime.now().strftime('%Y%m%d%H%M%S')
        pass

    def confirm_booking(self, request: BookingConfirmation) -> GenericResponse:
        pass

    def update_booking(self, request: CreateBooking) -> GenericResponse:
        pass

    def cancel_booking(self, request: CreateBooking) -> GenericResponse:
        pass

    def get_bookings_from_phone_number(self, phone_number: str) -> List[Booking]:
        pass

    def get_booking_from_booking_id(self, booking_id: str) -> Booking:
        pass

    def get_all_bookings(self, branch_id: str, date: str) -> List[Booking]:
        pass
