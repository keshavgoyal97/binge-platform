from app.constants import error_codes
from app.exceptions import Error, GenericException

KAFKA_POLL_MESSAGE_ERROR = Error(
    code=error_codes.KAFKA_POLL_MESSAGE_ERROR, message="Kafka Poll Error"
)


class KafkaMessagePollError(GenericException):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @property
    def error_code(self) -> str:
        return KAFKA_POLL_MESSAGE_ERROR.code
