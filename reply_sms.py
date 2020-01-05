#set up flask to auto respond to sms's with 
#resp.message
# requires you to run server (python run.py)
#requires you to run in another cmd
## twilio phone-numbers:update "+13347817392" --sms-url="http://localhost:5000/sms"
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import os

app = Flask(__name__)
directory = (__file__)
path = directory.replace(os.path.basename(__file__), r'Bills_CSVs\\')
test_txt = path + 'last_message.txt'

@app.route("/sms", methods=['POST'])
def sms_reply():
	number = request.form['From']
	message_body = request.form['Body']
	f= open(test_txt,'w+')
	f.write(message_body)
	f.close()
	resp = MessagingResponse()
	# resp.message('Hello {}, you said: {}'.format(number, message_body))
	# return(str(resp))
	

if __name__ == "__main__":
	app.run(debug=True)



