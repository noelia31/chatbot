import os, sys
from flask import Flask, request
from pymessenger import Bot
import ctypes


app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAAIZCyGuZBk7QBADaYDeZCAnDeMwvL8jFihXwdF7jZB0RFCxKmM8MZBXIUY5snXZCBC2AqsiyysbXrztnFFjOsRXNB0AczlmKcwbiTjri9sblZCpjMnjmaFV0OZC9DnYAWr59mYeNHZAE1szFleDJuOZAcniHtlvZBx5bMULX5JgpJTp78GelsZAmJNo"
bot =Bot(PAGE_ACCESS_TOKEN)
@app.route('/', methods = ['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return  request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods = ['POST'])
def Webhook():
	data = request.get_json()
	log(data)


	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:	

			    sender_id = messaging_event['sender']['id']
			    recipient_id = messaging_event['recipient']['id']

			    if messaging_event.get('message'):
			    	if 'text' in messaging_event['message']:
			    		messaging_text = messaging_event['message']['text']
			    	else:
			    		messaging_text = 'no text'
			    	#ECHO
			    	response = messaging_text
			    	bot.send_text_message(sender_id,response)
			    	
	return "ok",200		    	



def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=50000, debug=True)

    #app.run(debug=True, port=80)


