"""
The module hosts the exceptions of the app.
All exceptions in the app should extend the GenericException class
"""


from app.constants import error_codes


class Error:
    def __init__(self, code, message, http_code=500):
        self.code = code
        self.message = message
        self.http_code = http_code


GENERIC_INTERNAL_ERROR = Error(
    code=error_codes.INTERNAL_SERVER_ERROR, message="Internal server error"
)


class GenericException(Exception):
    def __init__(self, message=GENERIC_INTERNAL_ERROR.message, **kwargs) -> None:
        super().__init__(message)
        self.__message = f"{message}"
        self.__params = kwargs
        self.add_params(error_code=self.error_code)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def params(self) -> dict:
        return self.__params

    def add_params(self, **params) -> None:
        return self.__params.update(params)

    @property
    def status_code(self) -> int:
        """
        Returns the HTTP status code to be passed
        incase the exception is caught in the routes.
        """
        return GENERIC_INTERNAL_ERROR.http_code

    @property
    def error_code(self) -> str:
        """
        Returns the error code to represent
        the custom error codes for the service.
        """
        return GENERIC_INTERNAL_ERROR.code

    @property
    def should_notify(self) -> bool:
        """
        Returns if the error should be notified
        via error notifiers like Airbrake, Sentry.
        """
        return True
