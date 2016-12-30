import re
import random

############### HARAMBE ###############

def Harambe(message):
	if 'harambe' in message:
		return "DICKS OUT"
	return "-0"

############### You're Stupid ###############

def YoureStupid(lowerCaseMessage):
	lowerCaseMessage = lowerCaseMessage.replace("'", "")
	wordList = re.sub("[^\w]", " ", lowerCaseMessage).split()

	if wordList[-2] == "its" or wordList[-2] == "thats":
		return "You're " + wordList[-1] + "!"
	return "-0"

############### Know Her ###############

def KnowHer(wordList):
	last = wordList[-1]
	first = wordList[0]

	if len(last) > 3 and last[-1] == 'r' and last[-2] == 'e':
		return "{0} 'er? I hardly know her!".format(last[0:-2])

	elif len(first) > 3 and first[-1] == 'r' and first[-2] == 'e':
		return "{0} 'er? I hardly know her!".format(first[0:-2])
	
	return "-0"

############### Are you fucking me?! ###############

def AreYouFuckingMe():

	randNum = random.randrange(0, 100)
	if randNum == 20:
		return "Are you fucking me?!"
		
	return "-0"

############### Post Joe Pic ###############

def PostJoePic():
	randNum = random.randrange(0, 14)
	sNum = '20'

	if randNum == 0:
		picSuffix = 'v0r261evx/banana_Joe.jpg'
	if randNum == 1:
		picSuffix = 'p13b2du3h/blowjobjoe.jpg'
	if randNum == 2:
		picSuffix = 'prw185wgt/frenchmaidjoe.jpg'
	if randNum == 3:
		picSuffix = 'pt5z1kyal/Joeand_Nick.jpg'
	if randNum == 4:
		picSuffix = 'o2my03grh/joejames.jpg'
	if randNum == 5:
		picSuffix = '73ikykuxp/peacock_Joe.jpg'
	if randNum == 6:
		picSuffix = 'y2mftqhel/sexyyoungjoe.jpg'
	if randNum == 7:
		picSuffix = 'hg4vknogt/Sleepy_Joe1.jpg'
	if randNum == 8:
		picSuffix = '4d991dy8t/sleepyjoe2.jpg'
	if randNum == 9:
		picSuffix = 'nwduaqx0d/sleepyjoe3.jpg'
	if randNum == 10:
		picSuffix = 'epvjngrrx/sleepyjoe4.jpg'
	if randNum == 11:
		picSuffix = 'sktu5xm71/tyreejoe.jpg'
	if randNum == 12:
		picSuffix = 'a6jb1y9wd/xrayjoe.jpg'
	if randNum == 13:
		picSuffix = 'rl3ja8719/zombiejoe.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix


############### Post Maria Pic ###############	

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

############### Post Tyree Pic ###############	

def PostTyreePic():
	randNum = random.randrange(0, 40)
	sNum = '20'

	if randNum == 0:
		picSuffix = 'ism5qphgd/tyree_1.jpg'
	if randNum == 1:
		picSuffix = 'm0qn3r3q5/tyree_2.jpg'
	if randNum == 2:
		picSuffix = 'iv61djl3x/tyree_3.jpg'
	if randNum == 3:
		picSuffix = '4q08bqc2l/tyree_4.jpg'
	if randNum == 4:
		picSuffix = 'yj78kc0pp/tyree_5.jpg'
	if randNum == 5:
		picSuffix = '55bi4qxzx/tyree_6.jpg'
	if randNum == 6:
		picSuffix = 'giy1fy8il/tyree_7.jpg'
	if randNum == 7:
		picSuffix = 'fhxsqtrj1/tyree_8.jpg'
	if randNum == 8:
		picSuffix = 'jfl2g8ecd/tyree_9.jpg'
	if randNum == 9:
		picSuffix = 'e5g3oxu3h/tyree_10.jpg'
	if randNum == 10:
		picSuffix = 'e6umw3lb1/tyree_11.jpg'
	if randNum == 11:
		picSuffix = 'hez4957kt/tyree_12.jpg'
	if randNum == 12:
		picSuffix = 'ukemf91gd/tyree_13.jpg'
	if randNum == 13:
		picSuffix = 'g2hf79a59/tyree_14.jpg'
	if randNum == 14:
		picSuffix = 'f1h6i4t5p/tyree_15.jpg'
	if randNum == 15:
		picSuffix = 'vdr87v7h9/tyree_16.jpg'
	if randNum == 16:
		picSuffix = '6907ug80t/tyree_17.jpg'
	if randNum == 17:
		picSuffix = 'blp28kvx9/tyree_18.jpg'
	if randNum == 18:
		picSuffix = 'e4ar99hnh/tyree_19.jpg'
	if randNum == 19:
		picSuffix = 'd3aik50nx/tyree_20.jpg'
	if randNum == 20:
		picSuffix = 'v7i4iinq5/tyree_21.jpg'
	if randNum == 21:
		picSuffix = 'mdr81f0rh/tyree_22.jpg'
	if randNum == 22:
		picSuffix = 'ukj7szqu5/tyree_23.jpg'
	if randNum == 23:
		picSuffix = 'gfder6hst/tyree_24.jpg'
	if randNum == 24:
		picSuffix = 'rg8jw7a1p/tyree_25.jpg'
	if randNum == 25:
		picSuffix = 'eq4bj423h/tyree_26.jpg'
	if randNum == 26:
		picSuffix = '5jm0vtwv1/tyree_27.jpg'
	if randNum == 27:
		picSuffix = 'vgfp8g0il/tyree_28.jpg'
	if randNum == 28:
		picSuffix = 'or95sff6l/tyree_29.jpg'
	if randNum == 29:
		picSuffix = 'ev82ss9el/tyree_30.jpg'
	if randNum == 30:
		picSuffix = 'h16z1128t/tyree_31.jpg'
	if randNum == 31:
		picSuffix = 'ysilfhhnh/tyree_32.jpg'
	if randNum == 32:
		picSuffix = '3mtw4zvkt/tyree_33.jpg'
	if randNum == 33:
		picSuffix = '6i6zbuzkt/tyree_34.jpg'
	if randNum == 34:
		picSuffix = 'xhau70m1p/tyree_35.jpg'
	if randNum == 35:
		picSuffix = 'c8x5pl7kt/tyree_36.jpg'
	if randNum == 36:
		picSuffix = '5jqm9km8t/tyree_37.jpg'
	if randNum == 37:
		picSuffix = 'esssjov4t/tyree_38.jpg'
	if randNum == 38:
		picSuffix = 'wk4ey5ajh/tyree_39.jpg'
	if randNum == 39:
		picSuffix = 'gzx17m0f1/tyree_40.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### People Pics ###############

def PeoplePics(wordList):
	# Return list of urls to post
	returnURLS = []

	# Switches so we only post one pic per person
	joePosted = "false"
	mariaPosted = "false"
	tyreePosted = "false"

	for word in wordList:
		# Joe
		if word == 'joe' and joePosted == "false":
			joePosted = "true"
			returnURLS.append(PostJoePic())	
		
		# Maria / MC
		if (word == "maria" or word == "mc") and mariaPosted == "false":
			mariaPosted = "true"
			returnURLS.append(PostMariaPic())

		# Tyree
		if (word == "tyree" or word == "tree" or word == "tyreedo" or 
				word == "tyrizzle" or word == "tysizzle" or word == "tyrell" or
				word == "tyrone" or word == "tyrannosaurus" or word == "ty-ty" or
				word == "tyrhonda" or word == "tyrion" or word == "tyranny" or
				word == "typhoon" or word == "tycoon" or word == "tyrant" or
				word == "ty" or word == "tyrea" or word == "tymara" or
				word == "tyrkey" or word == "tyger" or word == "tycho" or
				word == "neckty" or word == "tyson" or word == "noty" or
				word == "tyedye" or word == "ty-dye" or word == "typhoid" or 
				word == "tyree-ree" or word == "ree-ree" or word == "tyred" or
				word == "tyke" or word == "typickle" or word == "typical" or
				word == "three" or word == "ty-chi" or word == "tyrella" or
				word == "tybrisa" or word == "rex") and tyreePosted == "false":
			tyreePosted = "true"
			returnURLS.append(PostTyreePic())

	return returnURLS
