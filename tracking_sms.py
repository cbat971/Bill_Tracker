#set up flask to auto respond to sms's with 
#resp.message
# requires you to run server (python run.py)
#requires you to run in another cmd
## twilio phone-numbers:update "+13347817392" --sms-url="http://localhost:5000/sms"
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import TwilioInfo as ti

SECRET_KEY = 'This_IS-a_sECRET'
app = Flask(__name__)
app.config.from_object(__name__)

callers = {
	ti.chris_num: "Chris",
	ti.haley_num: "Haley",
	ti.twilio_from: "Twilio",
}

@app.route("/sms", methods=['GET', 'POST'])
def hello():
	"""Respond with the number of text messages sent between two parties."""
	# Increment the counter
	counter = session.get('counter', 0)
	counter += 1

	#save counter value in the session
	session['counter'] = counter

	from_number = request.values.get('From')
	if from_number in callers:
		name = callers[from_number]
	else:
		name = "Friend"

	message = '{} has messaged {} {} times.' \
		.format(name, request.values.get('To'), counter)

	#Put it in a TwiML response
	resp = MessagingResponse()
	resp.message(message)

	return str(resp)



if __name__ == "__main__":
	app.run(debug=True)



