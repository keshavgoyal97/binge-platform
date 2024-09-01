from app.responses.generic_response import GenericResponse
from app.utils.logger import logger

_log = logger()


class UserService:

    def send_otp(self, phone_number: str) -> GenericResponse:
        _log.info("No record found for phone number {}".format(phone_number))

        pass

    def validate_otp(self, phone_number: str, otp: str) -> GenericResponse:
        pass
