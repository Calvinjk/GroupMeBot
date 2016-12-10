import re
import random

def Harambe(message):
	if 'harambe' in message:
		return "DICKS OUT"
	return "-0"

#######################################

def YoureStupid(lowerCaseMessage):
	lowerCaseMessage = lowerCaseMessage.replace("'", "")
	wordList = re.sub("[^\w]", " ", lowerCaseMessage).split()

	if wordList[-2] == "its" or wordList[-2] == "thats":
		return "You're " + wordList[-1] + "!"
	return "-0"

#######################################

def KnowHer(wordList):
	last = wordList[-1]
	first = wordList[0]

	if len(last) > 3 and last[-1] == 'r' and last[-2] == 'e':
		return "{0} 'er? I hardly know her!".format(last[0:-2])

	elif len(first) > 3 and first[-1] == 'r' and first[-2] == 'e':
		return "{0} 'er? I hardly know her!".format(first[0:-2])
	
	return "-0"

#######################################
def PostJoePic():
	randNum = random.randrange(0, 14)
	sNum = '12'

	if randNum == 0:
		picSuffix = 't62zmp0f1/banana_Joe.jpg'
	if randNum == 1:
		picSuffix = 'jzkozev6l/Joeand_Nick.jpg'
	if randNum == 2:
		picSuffix = 'c83z0ur19/peacock_Joe.jpg'
	if randNum == 3:
		picSuffix = '5ixfku5p9/Sleepy_Joe1.jpg'
	if randNum == 4:
		picSuffix = '5uzinsuin/sleepyjoe2.jpg'
	if randNum == 5:
		picSuffix = '4vyivb8t9/sleepyjoe3.jpg'
	if randNum == 6:
		picSuffix = '5zin79tgd/sleepyjoe4.jpg'
	if randNum == 7:
		sNum = '16'
		picSuffix = '9uqjishgx/blowjobjoe.jpg'
	if randNum == 8:
		sNum = '16'
		picSuffix = 'q70l8ivsh/frenchmaidjoe.jpg'
	if randNum == 9:
		sNum = '16'
		picSuffix = 'ej6jdz6nl/joejames.jpg'
	if randNum == 10:
		sNum = '16'
		picSuffix = 'crimg6tm9/sexyyoungjoe.jpg'
	if randNum == 11:
		sNum = '16'
		picSuffix = 'm0ksqb2i9/tyreejoe.jpg'
	if randNum == 12:
		sNum = '16'
		picSuffix = 'j7rl6a25t/xrayjoe.jpg'
	if randNum == 13:
		sNum = '16'
		picSuffix = 'pzi094r5d/zombiejoe.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

def PostMariaPic():
	randNum = random.randrange(0, 15)
	sNum = '17'

	if randNum == 0:
		picSuffix = 'uz2vnwhmn/maria_1.jpg'
	if randNum == 1:
		picSuffix = 's69o3vha7/maria_2.jpg'
	if randNum == 2:
		picSuffix = 'qsi18ki0v/maria_3.jpg'
	if randNum == 3:
		picSuffix = '5wvqxbltr/maria_4.jpg'
	if randNum == 4:
		picSuffix = 'ak1sz396n/maria_5.jpg'
	if randNum == 5:
		picSuffix = 'usp6kt8hr/maria_6.jpg'
	if randNum == 6:
		picSuffix = 'ndzusfmm7/maria_7.jpg'
	if randNum == 7:
		picSuffix = 'ao07t341r/maria_8.jpg'
	if randNum == 8:
		picSuffix = 'p8hanwz0f/maria_9.jpg'
	if randNum == 9:
		picSuffix = 'mfo33vynz/maria_10.jpg'
	if randNum == 10:
		picSuffix = '65xx0znzz/maria_11.jpg'
	if randNum == 11:
		picSuffix = '7m9fj4qwv/maria_12.jpg'
	if randNum == 12:
		picSuffix = 'mjhwk545b/maria_13.jpg'
	if randNum == 13:
		picSuffix = '7otb5yukf/maria_14.jpg'
	if randNum == 14:
		picSuffix = 'q5npwsain/maria_15.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

def PeoplePics(wordList):
	# Return list of urls to post
	returnURLS = []

	# Switches so we only post one pic per person
	joePosted = "false"
	mariaPosted = "false"

	for word in wordList:
		# Joe
		if word == 'joe' and joePosted == "false":
			joePosted = "true"
			returnURLS.append(PostJoePic())	
		
		# Maria / MC
		if word == "maria" or word == "mc" and mariaPosted == "false":
			mariaPosted = "true"
			returnURLS.append(PostMariaPic())

	return returnURLS

#######################################