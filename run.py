#set up flask to auto respond to sms's with 
#resp.message
# requires you to run server (python run.py)
#requires you to run in another cmd
## twilio phone-numbers:update "+13347817392" --sms-url="http://localhost:5000/sms"
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	"""Respond to incoming messages with a friendly SMS."""
	# Start our response
	resp = MessagingResponse()

	# Add a message
	resp.message("Ahoy! Thanks so much for your message.")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)



