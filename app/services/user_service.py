from __future__ import print_function

import random
from datetime import datetime
from app.models.all_info import AllInfo
from app.repository.meta_data import MetaDataRepository
from app.repository.user_login import UserLoginRepository
from app.models.generic_response import GenericResponse
from app.utils.logger import logger
from app.utils.config import get_config
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

_log = logger()

metaDataRepository = MetaDataRepository()
metadata = AllInfo()


class UserService:
    def __init__(self):
        self.login_repository = UserLoginRepository()
        self.metadata_repository = MetaDataRepository()

    def get_all_info(self) -> AllInfo:
        return metadata

    def update_metadata_file(self, new_theatre_json: str) -> GenericResponse:
        output = AllInfo.model_validate_json(new_theatre_json)
        json_output = output.model_dump(mode='json')
        success = self.metadata_repository.save_meta_data(json_output)
        if success:
            global metadata
            metadata = output
            return GenericResponse(success=True, error_code=None,
                                   error_message="Metadata file updated successfully")
        else:
            return GenericResponse(success=False, error_code=None,
                                   error_message="Unable to update Metadata file")

    def send_otp_through_sms(self, phone_number: str) -> GenericResponse:

        login_record = self.login_repository.get_otp_by_phone_number(phone_number=phone_number)
        if login_record and (datetime.now() - login_record.created_at).seconds <= 600:
            return GenericResponse(success=False, error_code=None,
                                   error_message="OTP has been already sent, its valid for 10mins.")

        otp = random.randint(100000, 999999)

        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = get_config("BREVO_API_KEY")

        get_config("OTP_MESSAGE")

        api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
        send_transac_sms = sib_api_v3_sdk.SendTransacSms(sender="HappyScreen", recipient="91" + phone_number,
                                                         content=get_config("OTP_MESSAGE").format(str(otp)),
                                                         type="transactional",
                                                         web_url=None)

        try:
            api_response = api_instance.send_transac_sms(send_transac_sms)
            pprint(api_response)
            _log.info("OTP has been sent to phone number {}".format(phone_number))

            success = self.login_repository.save_otp_and_phone_number(otp=str(otp), phone_number=phone_number)
            if success:
                return GenericResponse(success=True, error_code=None,
                                       error_message="OTP has been sent to your registered mobile number")
            else:
                return GenericResponse(success=False, error_code=None,
                                       error_message="Unable to save generated OTP")

        except ApiException as e:
            _log.error("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)
            return GenericResponse(success=False, error_code=None, error_message="Unable to send OTP")

    def send_otp_through_whatsapp(self, phone_number: str) -> GenericResponse:

        configuration = sib_api_v3_sdk.Configuration()
        key = get_config("BREVO_API_KEY")
        sender_number = get_config("SENDER_NUMBER")
        configuration.api_key['api-key'] = key

        api_instance = sib_api_v3_sdk.TransactionalWhatsAppApi(sib_api_v3_sdk.ApiClient(configuration))
        send_transac_whatsapp_message = sib_api_v3_sdk.SendWhatsappMessage(sender_number=sender_number,
                                                                           contact_numbers=["+91" + phone_number],
                                                                           text="Please use this OTP to update your "
                                                                                "booking, from "
                                                                                "https://www.thehappyscreens.in/")

        try:
            api_response = api_instance.send_whatsapp_message(send_transac_whatsapp_message)
            pprint(api_response)
        except ApiException as e:
            _log.error("Exception when calling TransactionalWhatsappApi->send_transac_sms: %s\n" % e)

        _log.info("OTP has been sent to phone number {}".format(phone_number))

    def validate_otp(self, phone_number: str, otp: str) -> GenericResponse:

        login_record = self.login_repository.get_otp_by_phone_number(phone_number=phone_number)
        if login_record:
            if login_record.otp == otp:
                return GenericResponse(success=True, error_code=None,
                                       error_message="OTP has been verified successfully")
            else:
                return GenericResponse(success=False, error_code=None,
                                       error_message="Latest OTP which was sent to your registered mobile number does not matches with entered one")
        else:
            return GenericResponse(success=False, error_code=None,
                                   error_message="No OTP record found for this phone number")
