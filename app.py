from flask import Flask,request
import requests
import re
import random
from helperFunctions import *
import logging
app = Flask(__name__)

def say(s):
	# USE THIS LINE FOR DEVELOPMENT
	if (s != "-0"):
		requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "088ef849ec340699ee3cbeabb8","text": s})
	
	# USE THIS LINE FOR LIVE
	# requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "2105543276296e8bd2fec9c082,"text": s})

@app.route('/', methods = ['GET', 'POST'])
def masterRunEverything():
	if request.method == 'GET':
		return 'This is the Test bot page.'

	if request.method == 'POST':
		message = request.get_json(force=True)
		lowerCaseMessage = message['text'].lower()
		wordList = re.sub("[^\w]", " ", lowerCaseMessage).split()

		# Make sure bot doesnt respond to own messages
		if message['name']!='Heroku "The Bot"':

			# Know her?
			say(KnowHer(wordList))
				
			# Harambe 
			say(Harambe(lowerCaseMessage))

			# Random People Pictures
			say(PeoplePics(wordList))

			# You're stupid!
			say(YoureStupid(lowerCaseMessage))

		return 'Fuckin test bot.'

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=80, debug=True)
