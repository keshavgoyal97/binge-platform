from typing import List, Optional
from datetime import datetime, timedelta

from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.booking import Booking
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_BOOKINGS_BY_BOOKING_ID = """SELECT * FROM booking WHERE booking_id = %(booking_id) and booking_status in ('PAYMENT_DONE', 'UPDATED') order by created_at desc"""
GET_BOOKINGS_BY_PHONE_NUMBER = """SELECT * FROM booking WHERE phone_number = %(phone_number) and created_at >= %(start_time) and booking_status in ('PAYMENT_DONE', 'UPDATED') order by created_at desc"""
GET_BOOKINGS_FOR_TOMORROW = """SELECT * FROM booking WHERE created_at between %(start_time) and %(end_time) and booking_status in ('PAYMENT_DONE', 'UPDATED') order by created_at desc"""
GET_BOOKINGS_BY_THEATRE_ID = """SELECT * FROM booking WHERE booking_date = %(booking_date) and theatre_id = %(theatre_id) and booking_status in ('PAYMENT_DONE', 'UPDATED') order by created_at desc"""
GET_BOOKINGS_BY_BRANCH_ID = """SELECT * FROM booking WHERE booking_date = %(booking_date) and branch_id = %(branch_id) order by created_at desc"""
CANCEL_BOOKING = """UPDATE booking SET booking_status='CANCELLED' WHERE booking_id = %(booking_id)"""


# today = datetime.now()
# tomorrow = datetime.now() + timedelta(days=1)
# start_time = today.replace(hour=0, minute=0, second=0, microsecond=0)
# end_time = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)


def transform_db_results_to_booking_objects(records) -> List[Booking]:
    output = []
    for record in records:
        if record is not None:
            booking = Booking(
                created_by=record[2],
                admin_name=record[2],
                created_at=record[2],
                last_updated_at=record[2],
                status=record[2],
                booking_name=record[2],
                booking_date=record[2],
                start_time=record[2],
                end_time=record[2],
                theatre_id=record[2],
                branch_id=record[2],
                email=record[2],
                phone_number=record[2],
                total_price=record[2],
                advance_paid=record[2],
                number_of_people=record[2],
                decor_type=record[2],
                decor_name_1=record[2],
                decor_name_2=record[2],
                add_on_ids=record[2],
                cake_ids=record[2],
                duration=record[2],
            )
            output.append(booking)

    return output


def transform_db_result_to_booking_object(record) -> Optional[Booking]:
    if record is not None:
        booking = Booking(
            created_by=record[2],
            admin_name=record[2],
            created_at=record[2],
            last_updated_at=record[2],
            status=record[2],
            booking_name=record[2],
            booking_date=record[2],
            start_time=record[2],
            end_time=record[2],
            theatre_id=record[2],
            branch_id=record[2],
            email=record[2],
            phone_number=record[2],
            total_price=record[2],
            advance_paid=record[2],
            number_of_people=record[2],
            decor_type=record[2],
            decor_name_1=record[2],
            decor_name_2=record[2],
            add_on_ids=record[2],
            cake_ids=record[2],
            duration=record[2],
        )
        return booking
    else:
        return None


class BookingRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_booking_from_booking_id(self, booking_id: str) -> Optional[Booking]:
        try:
            record = self.db.fetch_all(
                GET_BOOKINGS_BY_BOOKING_ID, {"booking_id": booking_id}
            )

            booking = transform_db_result_to_booking_object(record)
            if not booking:
                _log.info("No booking records found for booking_id {}".format(booking_id))
            return booking

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, booking_id)

    def get_bookings_by_phone_number(self, phone_number: str, start_time: str) -> List[Booking]:
        try:
            records = self.db.fetch_all(
                GET_BOOKINGS_BY_PHONE_NUMBER, {"phone_number": phone_number, "start_time": start_time}
            )

            bookings = transform_db_results_to_booking_objects(records)
            if not bookings:
                _log.info("No booking records found for phone_number {}".format(phone_number))
            return bookings

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, phone_number)

    def get_bookings_for_tomorrow(self, start_time: str, end_time: str):

        try:
            records = self.db.fetch_all(
                GET_BOOKINGS_FOR_TOMORROW, {"start_time": start_time, "end_time": end_time}
            )

            bookings = transform_db_results_to_booking_objects(records)
            if not bookings:
                _log.info("No booking records found for start_time {}, end_time {}".format(start_time, end_time))
            return bookings

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, start_time)

    def get_bookings_for_theatre_id(self, booking_date: str, theatre_id: str):

        try:
            records = self.db.fetch_all(
                GET_BOOKINGS_BY_THEATRE_ID, {"booking_date": booking_date, "theatre_id": theatre_id}
            )

            bookings = transform_db_results_to_booking_objects(records)
            if not bookings:
                _log.info(
                    "No booking records found for booking_date {}, theatre_id {}".format(booking_date, theatre_id))
            return bookings

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, theatre_id)

    def get_bookings_for_branch_id(self, booking_date: str, branch_id: str):

        try:
            records = self.db.fetch_all(
                GET_BOOKINGS_BY_BRANCH_ID, {"booking_date": booking_date, "branch_id": branch_id}
            )

            bookings = transform_db_results_to_booking_objects(records)
            if not bookings:
                _log.info(
                    "No booking records found for booking_date {}, theatre_id {}".format(booking_date, theatre_id))
            return bookings

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, theatre_id)

    def cancel_booking(self, booking_id: str):

        try:
            records = self.db.execute(
                CANCEL_BOOKING, {"booking_id": booking_id}
            )

            if records is not None:
                return True
            else:
                _log.info(
                    "No booking records found for cancellation, booking_id {}".format(booking_id))
                return False

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, booking_id)
