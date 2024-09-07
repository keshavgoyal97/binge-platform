from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.admin_user import AdminUser
from app.models.booking import Booking
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_BOOKINGS_BY_PHONE_NUMBER = """SELECT * FROM booking WHERE phone_number = %(phone_number) and booking_status='PAYMENT_DONE' order by created_at desc"""


class TransactionRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_bookings_by_phone_number(self, phone_number):
        try:
            record = self.db.fetch_one(
                GET_BOOKINGS_BY_PHONE_NUMBER, {"phone_number": phone_number}
            )
            if record is not None:
                user = Booking(
                    admin_type=record[2],
                    user_id=record[3],
                    password=record[4],
                    created_at=record[5]
                )
                return user
            _log.info("No booking records found for phone_number {}".format(phone_number))
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, phone_number)
