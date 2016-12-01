from flask import Flask,request
import requests
import re
app = Flask(__name__)

print 'run'

def say(s):
	requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "b24ce747ab0015068a61460d85","text": s})

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
	print 'viewed'
 	return 'This is the Test bot page.'

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
