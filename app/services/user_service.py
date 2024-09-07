from app.models.all_info import AllInfo
from app.repository.meta_data import MetaDataRepository
from app.requests.get_slots_request import GetSlotsRequest
from app.responses.generic_response import GenericResponse
from app.utils.logger import logger

_log = logger()

metaDataRepository = MetaDataRepository()


class UserService:

    def get_all_info(self) -> AllInfo:
        return metaDataRepository.get_latest_meta_data()

    def get_slots(self, request: GetSlotsRequest) -> List[SlotAvailabilityInfo]:
        pass

    def send_otp(self, phone_number: str) -> GenericResponse:
        _log.info("No record found for phone number {}".format(phone_number))

        pass

    def validate_otp(self, phone_number: str, otp: str) -> GenericResponse:
        pass
