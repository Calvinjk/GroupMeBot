from flask import Flask,request
import requests
import re
import random
from helperFunctions import *
import logging
app = Flask(__name__)

print 'run'

def say(s):
	# USE THIS LINE FOR LIVE
	requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "088ef849ec340699ee3cbeabb8","text": s})
	
	# USE THIS LINE FOR DEVELOPMENT 
	# requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "088ef849ec340699ee3cbeabb8","text": s})

@app.route('/', methods = ['GET', 'POST'])
def masterRunEverything():
	if request.method == 'GET':
		print 'viewed'
		return 'This is the Test bot page.'

	if request.method == 'POST':
		message = request.get_json(force=True)
		if message['name']!='Heroku "The Bot"':

			#Know her?
			wordList = re.sub("[^\w]", " ", message['text'].lower()).split()
			last = wordList[-1]
			first = wordList[0]
			
			if len(last) > 3 and last[-1] == 'r' and last[-2] == 'e':
				say("{0} 'er? I hardly know her!".format(last[0:-2]))
				print 'got em'
			elif len(first) > 3 and first[-1] == 'r' and first[-2] == 'e':
				say("{0} 'er? I hardly know her!".format(first[0:-2]))
				
			#Harambe 
			say(Harambe(message['text'].lower()))

			#Random People Pictures
			wordList = re.sub("[^\w]", " ", message['text'].lower()).split()
			for word in wordList:

				# Joe
				if word == 'joe':
					randNum = random.randrange(0, 14)
					sNum = '12'

					if randNum == 0:
						picSuffix = 't62zmp0f1/banana_Joe.jpg';
					if randNum == 1:
						picSuffix = 'jzkozev6l/Joeand_Nick.jpg';
					if randNum == 2:
						picSuffix = 'c83z0ur19/peacock_Joe.jpg';
					if randNum == 3:
						picSuffix = '5ixfku5p9/Sleepy_Joe1.jpg';
					if randNum == 4:
						picSuffix = '5uzinsuin/sleepyjoe2.jpg';
					if randNum == 5:
						picSuffix = '4vyivb8t9/sleepyjoe3.jpg';
					if randNum == 6:
						picSuffix = '5zin79tgd/sleepyjoe4.jpg';
					if randNum == 7:
						sNum = '16'
						picSuffix = '9uqjishgx/blowjobjoe.jpg';
					if randNum == 8:
						sNum = '16'
						picSuffix = 'q70l8ivsh/frenchmaidjoe.jpg';
					if randNum == 9:
						sNum = '16'
						picSuffix = 'ej6jdz6nl/joejames.jpg';
					if randNum == 10:
						sNum = '16'
						picSuffix = 'crimg6tm9/sexyyoungjoe.jpg';
					if randNum == 11:
						sNum = '16'
						picSuffix = 'm0ksqb2i9/tyreejoe.jpg';
					if randNum == 12:
						sNum = '16'
						picSuffix = 'j7rl6a25t/xrayjoe.jpg';
					if randNum == 13:
						sNum = '16'
						picSuffix = 'pzi094r5d/zombiejoe.jpg';

					say('https://s' + sNum + '.postimg.org/' + picSuffix)	
					break

		return 'Fuckin test bot.'

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=80, debug=True)
