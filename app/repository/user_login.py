from typing import Optional

from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.user_login import UserLogin
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_OTP_BY_PHONE_NUMBER = """SELECT * FROM login WHERE phone_number = %(phone_number) order by created_at desc"""
SAVE_OTP_AND_PHONE_NUMBER = """INSERT INTO login (otp, phone_number) values (%(otp), %(phone_number))"""


class UserLoginRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_otp_by_phone_number(self, phone_number) -> Optional[UserLogin]:
        try:
            record = self.db.fetch_one(
                GET_OTP_BY_PHONE_NUMBER, {"phone_number": phone_number}
            )
            if record is not None:
                user = UserLogin(
                    otp=record[1],
                    phone_number=record[2],
                    created_at=record[3]
                )
                return user
            _log.info("No record found for otp with phone_number {}".format(phone_number))
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, phone_number)

    def save_otp_and_phone_number(self, otp: str, phone_number: str) -> bool:
        try:
            record = self.db.execute(
                SAVE_OTP_AND_PHONE_NUMBER, {"otp": otp, "phone_number": phone_number}
            )
            if record is not None:
                return True
            else:
                _log.info("Unable to save otp {} and phone_number {}".format(otp, phone_number))
                return False
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, phone_number)
