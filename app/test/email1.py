from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key[
    'api-key'] = "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"

api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
send_transac_sms = sib_api_v3_sdk.SendTransacSms(sender="HappyScreen", recipient="918011027300",
                                                 content="first message",
                                                 type="transactional",
                                                 web_url=None)

try:
    api_response = api_instance.send_transac_sms(send_transac_sms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)

api_instance1 = sib_api_v3_sdk.TransactionalWhatsAppApi(sib_api_v3_sdk.ApiClient(configuration))
send_transac_whatsapp_message = sib_api_v3_sdk.SendWhatsappMessage(sender_number="9109846454",
                                                                   contact_numbers=["918011027300"],
                                                                   text="first message")

try:
    api_response = api_instance1.send_whatsapp_message(send_transac_whatsapp_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalWhatsappApi->send_transac_sms: %s\n" % e)
