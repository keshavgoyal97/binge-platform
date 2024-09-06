from app.exceptions import GENERIC_INTERNAL_ERROR, GenericException
from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException


class ErrorResponse:
    @staticmethod
    def builder(exception: Exception) -> dict:
        if isinstance(exception, GenericException):
            error = {
                "code": exception.error_code,
                "message": exception.message,
            }

        elif isinstance(exception, HTTPException):
            error = {
                "code": f"REF_RECOM_{exception.status_code}",
                "message": exception.detail,
            }
        else:
            error = {
                "code": GENERIC_INTERNAL_ERROR.code,
                "message": GENERIC_INTERNAL_ERROR.message,
            }
        return {"success": False, "error": error}
