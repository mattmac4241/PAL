import os

from twilio.rest import TwilioRestClient

account = os.environ.get("TWILIO_ACCOUNT")
token = os.environ.get("TWILIO_TOKEN")


def send_message(to, body):
    client = TwilioRestClient(account, token)
    client.sms.messages.create(
        to=to, from_=os.environ.get("TWILIO_NUMBER"), body=body)
