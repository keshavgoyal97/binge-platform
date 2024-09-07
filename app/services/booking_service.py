from pprint import pprint
from typing import List

import sib_api_v3_sdk
from fastapi_utilities import repeat_at
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.models.booking import Booking
from app.models.slot_availability_info import SlotAvailabilityInfo
from app.repository.booking import BookingRepository
from app.requests.confirm_booking import BookingConfirmation
from app.models.generic_response import GenericResponse
from app.requests.get_slots_request import GetSlotsRequest
from app.utils.config import get_config
from app.utils.logger import logger

from datetime import datetime

_log = logger()


def send_booking_email_for_free(booking: Booking) -> bool:
    receiver_email = booking.email

    try:
        # Configuration
        port = get_config("EMAIL_PORT")
        smtp_server = get_config("EMAIL_HOST")
        login = get_config("EMAIL_HOST_USER")
        password = get_config("EMAIL_HOST_PASSWORD")
        sender_email = get_config("EMAIL_SENDER_EMAIL")

        # Email content
        subject = "Booking confirmation with The Happy Screens"
        html = """\
        <html>
          <body>
            <p>Hi,<br>
            This is a <b>test</b> email without an attachment sent using <a href="https://www.python.org">Python</a>.</p>
          </body>
        </html>
        """

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach the HTML part
        message.attach(MIMEText(html, "html"))

        # Send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        _log.info('Booking email has been sent successfully to' + receiver_email)
        return True
    except Exception as e:
        _log.error('Error while sending booking email to ' + receiver_email, e)
        return False


def send_booking_email(booking: Booking) -> bool:
    try:
        sender_email = get_config("EMAIL_SENDER_EMAIL")
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = get_config("BREVO_API_KEY")
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        receiver_email = booking.email
        sender = {"email": sender_email}
        html_content = """\
        <html>
          <body>
            <p>Hi,<br>
            This is a <b>test</b> email without an attachment sent using <a href="https://www.python.org">Python</a>.</p>
          </body>
        </html>
        """
        subject = "Thanks for booking with The Happy Screens"
        to_field = [
            {
                "email": receiver_email,
                "name": booking.booking_name
            }
        ]

        smtp_template = sib_api_v3_sdk.SendSmtpEmail(sender=sender, html_content=html_content,
                                                     subject=subject, to=to_field, reply_to=sender,
                                                     )

        api_response = api_instance.send_transac_email(smtp_template)
        pprint(api_response)
        _log.info('Email has been sent to' + receiver_email)
        return True

    except Exception as e:
        _log.error("Exception when calling SMTPApi->post_email: %s\n" % e)
        return False


class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()

    def create_booking(self, request: Booking) -> GenericResponse:
        # Generate a timestamp-based ID
        timestamp_id = 'B' + datetime.now().strftime('%Y%m%d%H%M%S')
        pass

    def confirm_booking(self, request: BookingConfirmation) -> GenericResponse:
        pass

    def update_booking(self, request: Booking) -> GenericResponse:
        pass

    def cancel_booking(self, booking_id: str) -> GenericResponse:
        return self.booking_repository.cancel_booking(booking_id=booking_id)

    def get_bookings_from_phone_number(self, phone_number: str) -> List[Booking]:
        return self.booking_repository.get_bookings_by_phone_number(phone_number=phone_number)

    def get_booking_from_booking_id(self, booking_id: str) -> Booking:
        return self.booking_repository.get_booking_from_booking_id(booking_id=booking_id)

    def get_all_bookings(self, branch_id: str, date: str) -> List[Booking]:
        return self.booking_repository.get_bookings_for_branch_id(booking_date=date, branch_id=branch_id)

    def get_slots(self, request: GetSlotsRequest) -> List[SlotAvailabilityInfo]:
        pass

    @repeat_at(cron="0 5 * * *")
    async def send_reminder(self):
        print("hey")
