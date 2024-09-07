from typing import Union

from app.constants import error_codes
from app.exceptions import Error, GenericException

UPSERT_ONBOARDING_SOURCE_EXCEPTION = Error(
    code=error_codes.UPSERT_ONBOARDING_SOURCE_EXCEPTION,
    message="Error while upsert - onboarding source",
)
UPSERT_ONBOARDING_COMPLETED_STATUS_EXCEPTION = Error(
    code=error_codes.UPSERT_ONBOARDING_COMPLETED_STATUS_EXCEPTION,
    message="Error while upsert - onboarding completed status",
)
UPSERT_ONBOARDING_WAITLISTED_STATUS_EXCEPTION = Error(
    code=error_codes.UPSERT_ONBOARDING_WAITLISTED_STATUS_EXCEPTION,
    message="Error while upsert - onboarding waitlisted status",
)
UPSERT_TRANSACTED_STATUS_EXCEPTION = Error(
    code=error_codes.UPSERT_TRANSACTED_STATUS_EXCEPTION,
    message="Error while upsert - transacted status",
)
UPSERT_GCL_EXCEPTION = Error(
    code=error_codes.UPSERT_GCL_EXCEPTION,
    message="Error while upsert - GCL",
)
UPSERT_MCL_EXCEPTION = Error(
    code=error_codes.UPSERT_MCL_EXCEPTION,
    message="Error while upsert - MCL",
)
DELETE_GCL_EXCEPTION = Error(
    code=error_codes.DELETE_GCL_EXCEPTION,
    message="Error while delete - GCL",
)
DELETE_MCL_EXCEPTION = Error(
    code=error_codes.DELETE_MCL_EXCEPTION,
    message="Error while delete - MCL",
)
FETCH_ONE_EXCEPTION = Error(
    code=error_codes.FETCH_ONE_EXCEPTION,
    message="Error while fetch one",
)
FETCH_MANY_EXCEPTION = Error(
    code=error_codes.FETCH_MANY_EXCEPTION,
    message="Error while fetch many",
)


class UpsertOnboardingSourceException(GenericException):
    def __init__(
        self, ex: Exception, phone_number: str, onboarding_source: str
    ) -> None:
        message = UPSERT_ONBOARDING_SOURCE_EXCEPTION.message
        super().__init__(
            message,
            phone_number=phone_number,
            onboarding_source=onboarding_source,
            ex=ex.__str__(),
        )

    @property
    def error_code(self) -> str:
        return UPSERT_ONBOARDING_SOURCE_EXCEPTION.code


class UpsertOnboardingCompletedStatusException(GenericException):
    def __init__(self, ex: Exception, phone_number: str) -> None:
        message = UPSERT_ONBOARDING_COMPLETED_STATUS_EXCEPTION.message
        super().__init__(message, phone_number=phone_number, ex=ex.__str__())

    @property
    def status_code(self) -> int:
        return UPSERT_ONBOARDING_COMPLETED_STATUS_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return UPSERT_ONBOARDING_COMPLETED_STATUS_EXCEPTION.code


class UpsertOnboardingWaitlistedStatusException(GenericException):
    def __init__(self, ex: Exception, phone_number: str) -> None:
        message = UPSERT_ONBOARDING_WAITLISTED_STATUS_EXCEPTION.message
        super().__init__(message, phone_number=phone_number, ex=ex.__str__())

    @property
    def status_code(self) -> int:
        return UPSERT_ONBOARDING_WAITLISTED_STATUS_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return UPSERT_ONBOARDING_WAITLISTED_STATUS_EXCEPTION.code


class UpsertTransactedStatusException(GenericException):
    def __init__(self, ex: Exception, phone_number: str) -> None:
        message = UPSERT_TRANSACTED_STATUS_EXCEPTION.message
        super().__init__(message, phone_number=phone_number, ex=ex.__str__())

    @property
    def status_code(self) -> int:
        return UPSERT_TRANSACTED_STATUS_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return UPSERT_TRANSACTED_STATUS_EXCEPTION.code


class UpsertGlobalCreditLineException(GenericException):
    def __init__(self, ex: Exception, phone_number: str, credit_line: str) -> None:
        message = UPSERT_GCL_EXCEPTION.message
        super().__init__(
            message,
            phone_number=phone_number,
            credit_line=credit_line,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return UPSERT_GCL_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return UPSERT_GCL_EXCEPTION.code


class UpsertMerchantCreditLineException(GenericException):
    def __init__(self, ex: Exception, phone_number: str, credit_line: str) -> None:
        message = UPSERT_MCL_EXCEPTION.message
        super().__init__(
            message,
            phone_number=phone_number,
            credit_line=credit_line,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return UPSERT_MCL_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return UPSERT_MCL_EXCEPTION.code


class DeleteGlobalCreditLineException(GenericException):
    def __init__(self, ex: Exception, phone_number: str, credit_line: str) -> None:
        message = DELETE_GCL_EXCEPTION.message
        super().__init__(
            message,
            phone_number=phone_number,
            credit_line=credit_line,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return DELETE_GCL_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return DELETE_GCL_EXCEPTION.code


class DeleteMerchantCreditLineException(GenericException):
    def __init__(self, ex: Exception, phone_number: str, credit_line: str) -> None:
        message = DELETE_MCL_EXCEPTION.message
        super().__init__(
            message,
            phone_number=phone_number,
            credit_line=credit_line,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return DELETE_MCL_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return DELETE_MCL_EXCEPTION.code


class FetchOneUserMetadataException(GenericException):
    def __init__(self, ex: Exception, id: str) -> None:
        message = FETCH_ONE_EXCEPTION.message
        super().__init__(
            message,
            id=id,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return FETCH_ONE_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return FETCH_ONE_EXCEPTION.code


class FetchManyUserMetadataException(GenericException):
    def __init__(
        self, ex: Exception, phone_numbers: Union[list[str], set[str]]
    ) -> None:
        message = FETCH_MANY_EXCEPTION.message
        super().__init__(
            message,
            phone_numbers=phone_numbers,
            ex=ex.__str__(),
        )

    @property
    def status_code(self) -> int:
        return FETCH_MANY_EXCEPTION.http_code

    @property
    def error_code(self) -> str:
        return FETCH_MANY_EXCEPTION.code
