from app.models.admin_user import AdminUser
from app.repository.admin_user import AdminUserRepository
from app.repository.booking import BookingRepository
from app.requests.login_request import LoginRequest
from app.models.generic_response import GenericResponse
from app.models.login_response import LoginResponse
from app.utils.config import get_config
from app.utils.logger import logger
from jinja2 import Template
import pdfkit
import sib_api_v3_sdk
from pprint import pprint
import tempfile

_log = logger()


def upload_bill(pdf_output_path: str) -> str:
    pass


def send_booking_bill(pdf_output_url: str, receiver_email: str) -> bool:
    try:
        sender_email = get_config("EMAIL_SENDER_EMAIL")
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = get_config("BREVO_API_KEY")
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        sender = {"email": sender_email}
        html_content = """\
            <html>
              <body>
                <p>
                Hi,<br>
                Please find the attached booking GST Invoice.<br><br>
                
                Thanks<br>
                The Happy Screens<br>
              </body>
            </html>
            """
        subject = "Please find the attached booking invoice, from The Happy Screens"
        to_field = [
            {
                "email": receiver_email
            }
        ]

        smtp_template = sib_api_v3_sdk.SendSmtpEmail(sender=sender, html_content=html_content,
                                                     subject=subject, to=to_field, reply_to=sender,
                                                     attachment=pdf_output_url)

        api_response = api_instance.send_transac_email(smtp_template)
        _log.info('Bill has been sent to' + receiver_email)
        pprint(api_response)
        return True

    except Exception as e:
        _log.error("Exception when calling SMTPApi->post_email: %s\n" % e)
        return False


class AdminService:
    def __init__(self):
        self.admin_repository = AdminUserRepository()
        self.booking_repository = BookingRepository()

    def admin_login(self, request: LoginRequest) -> LoginResponse:
        admin_user = self.admin_repository.get_user_by_user_id(user_id=request.user_id)
        if admin_user:
            if admin_user.password == request.password:
                return LoginResponse(success=True, error_message=None, admin_type=admin_user.admin_type)
            else:
                return LoginResponse(success=False, error_message="Incorrect password", admin_type=None)
        else:
            return LoginResponse(success=False, error_message="User Id does not exists", admin_type=None)

    def generate_bill(self, booking_id: str) -> GenericResponse:
        booking = self.booking_repository.get_booking_from_booking_id(booking_id=booking_id)
        if booking:
            try:
                with open('invoice_format.html', 'r') as file:
                    content = file.read()
                    template = Template(content)
                    base_price = booking.total_price // 1.18
                    tax = booking.total_price - base_price
                    rendered_template = template.render(name=booking.booking_name, phone_number=booking.phone_number,
                                                        email=booking.email,
                                                        date=booking.booking_date.strftime("%b %d, %Y"),
                                                        total_amount=booking.total_price, tax=tax / 2,
                                                        base_price=base_price)

                    pdf_output_path = tempfile.TemporaryFile()
                    pdfkit.from_string(rendered_template, pdf_output_path)
                    pdf_output_url = upload_bill(pdf_output_path)

                    send_booking_bill(pdf_output_url, booking.email)
                    _log.info(f"PDF generated at {pdf_output_path} and saved at {pdf_output_url}")

                return GenericResponse(success=True, error_code=None, error_message=None)
            except Exception as e:
                return GenericResponse(success=False, error_code=None,
                                       error_message="Exception while generating the Invoice")

        else:
            return GenericResponse(success=False, error_code=None,
                                   error_message="No successful booking found for this booking_id")

    def create_user(self, new_user: AdminUser) -> GenericResponse:
        new_admin_user = self.admin_repository.save_user(admin_type=new_user.admin_type, user_id=new_user.user_id,
                                                         password=new_user.password)

        if new_admin_user:
            return GenericResponse(success=True, error_code=None, error_message=None)
        else:
            return GenericResponse(success=False, error_code=None, error_message="Unable to create new user")

    def delete_user(self, user_id: str) -> GenericResponse:
        admin_user = self.admin_repository.delete_user(user_id=user_id)

        if admin_user:
            return GenericResponse(success=True, error_code=None, error_message=None)
        else:
            return GenericResponse(success=False, error_code=None, error_message="Unable to delete user")
