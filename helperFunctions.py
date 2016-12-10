def say(s):
	# USE THIS LINE FOR LIVE
	requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "088ef849ec340699ee3cbeabb8","text": s})
	
	# USE THIS LINE FOR DEVELOPMENT 
	# requests.post('https://api.groupme.com/v3/bots/post', data = {"bot_id": "088ef849ec340699ee3cbeabb8","text": s})


def Harambe(message):
	if 'harambe' in message:
		say("DICKS OUT")






