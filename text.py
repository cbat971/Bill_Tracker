from twilio.rest import Client
import os
import TwilioInfo as ti


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
def text(body_text):
	client = Client(account_sid, auth_token)
	message = client.messages \
				.create(
					body=str(body_text),
					from_= ti.twilio_from,
					to = ti.chris_num
					)
	print(message.body)
def text_wife(body_text):
	client = Client(account_sid, auth_token)
	message = client.messages \
				.create(
					body=str(body_text),
					from_= ti.twilio_from,
					to= ti.haley_num
					)
	print(message.body)	

