from twilio.rest import Client
import os

print('The TWILIO_ACCOUNT_SID is ' + os.environ['TWILIO_ACCOUNT_SID'])
print('The TWILIO_AUTH_TOKEN is ' + os.environ['TWILIO_AUTH_TOKEN'])
client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
message = client.messages \
			.create(
				body="Testing.",
				from_= '+13347817392',
				to='+13364573067'
				)
print(message.body)			


