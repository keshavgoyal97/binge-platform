from app.models.admin_user import AdminUser
from app.models.theatre import Theatre
from app.requests.login_request import LoginRequest
from app.responses.generic_response import GenericResponse
from app.responses.login_response import LoginResponse
from app.utils.logger import logger

_log = logger()


class AdminService:

    def admin_login(self, request: LoginRequest) -> LoginResponse:
        _log.info("No record found for phone number {}")
        pass

    def generate_bill(self, booking_id: str) -> GenericResponse:
        pass

    def create_user(self, new_user: AdminUser) -> GenericResponse:
        pass

    def delete_user(self, user_id: str) -> GenericResponse:
        pass

    def add_branch(self, new_theatre_json: str) -> GenericResponse:
        Theatre.model_validate_json(new_theatre_json)
        pass
