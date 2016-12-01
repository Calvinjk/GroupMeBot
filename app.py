from flask import Flask,request
import requests
import re
import random
app = Flask(__name__)

print 'run'

def say(s):
	requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "2105543276296e8bd2fec9c082","text": s})

@app.route('/', methods = ['GET', 'POST'])
def masterRunEverything():
	if request.method == 'GET':
		print 'viewed'
		return 'This is the Test bot page.'

	if request.method == 'POST':
		message = request.get_json(force=True)
		if message['name']!='Heroku "The Bot"':

			#Know her?
			
			#me = re.compile("\\b\\w+er\\b")
			#m = me.findall(message['text'])
			
			wordList = re.sub("[^\w]", " ", message['text'].lower()).split()
			last = wordList[-1]
			first = wordList[0]
			
			if len(last) > 3 and last[-1] == 'r' and last[-2] == 'e':
				say("{0} 'er? I hardly know her!".format(last[0:-2]))
			elif len(first) > 3 and first[-1] == 'r' and first[-2] == 'e':
				say("{0} 'er? I hardly know her!".format(first[0:-2]))
				

			#Harambe 
			if 'harambe' in message['text'].lower():
						say("DICKS OUT")

			#Random Joe Pictures
			wordList = re.sub("[^\w]", " ", message['text'].lower()).split()
			for word in wordList:
				if word == 'joe':
					randNum = random.randrange(0, 7)

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

					say('https://s12.postimg.org/' + picSuffix)	
					break

		return 'Fuckin test bot.'


#@app.route('/', methods = ['POST'])
# def respond():
# 	message = request.get_json(force=True)
# 	if message['name']!='Test Bot':
# 		#if message['name'] == 'Michael Siciliano':
# 			#say('Hi Mike, good to hear from you.')

# 		me=re.compile("\\b\\w+er\\b")
# 		m=me.findall(message['text'])
# 		for x in m:
# 			if len(x)>3:
# 				say("{0} her? I hardly know her!".format(x[0:-2]))

# 		#if 'just a gorilla' in message['text'].lower():
# 			#say("https://i.groupme.com/750x500.jpeg.8987479304894b409885460900141d47")

# 		elif 'harambe' in message['text'].lower():
# 			say("DICKSOUT")

# @app.route('/say', methods = ['GET'])
# def send():
# 	say('DICKSOUT')

# 	return 'said dicksout.'

if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=80, debug=True)
