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
	randNum = random.randrange(0, 15)
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
	if randNum == 14:
		picSuffix = 'hmimbaa3h/mousejoe.jpg'

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

############### Post Alexis Pic ###############	

def PostAlexisPic():
	randNum = random.randrange(0, 18)
	sNum = '20'

	if randNum == 0:
		picSuffix = 's0wrqdi1p/alexis_1.jpg'
	if randNum == 1:
		picSuffix = 'ngalbfycd/alexis_2.jpg'
	if randNum == 2:
		picSuffix = '6tt12d5el/alexis_3.jpg'
	if randNum == 3:
		picSuffix = '65k6jf6ot/alexis_4.jpg'
	if randNum == 4:
		picSuffix = 'ecc6azwrh/alexis_5.jpg'
	if randNum == 5:
		picSuffix = 'h7p9hv0rh/alexis_6.jpg'
	if randNum == 6:
		picSuffix = 'bkswkdy8t/alexis_7.jpg'
	if randNum == 7:
		picSuffix = 'ueephdwgt/alexis_8.jpg'
	if randNum == 8:
		picSuffix = '6bxvmiftp/alexis_9.jpg'
	if randNum == 9:
		picSuffix = '6d7tfxhnh/alexis_10.jpg'
	if randNum == 10:
		picSuffix = 'anr2p9c4d/alexis_11.jpg'
	if randNum == 11:
		picSuffix = '6snomosyl/alexis_12.jpg'
	if randNum == 12:
		picSuffix = 'vzykmxw2l/alexis_13.jpg'
	if randNum == 13:
		picSuffix = 'oy0n0qsgt/alexis_14.jpg'
	if randNum == 14:
		picSuffix = 'xubf4oj31/alexis_15.jpg'
	if randNum == 15:
		picSuffix = 'imvfkbr8d/alexis_16.jpg'
	if randNum == 16:
		picSuffix = '578euviqj/alexis_17.jpg'
	if randNum == 17:
		picSuffix = 'w6c9q157h/alexis_18.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### Post Rudy Pic ###############	

def PostRudyPic():
	randNum = random.randrange(0, 23)
	sNum = '20'

	if randNum == 0:
		picSuffix = 'uvir65uot/rudy_1.jpg'
	if randNum == 1:
		picSuffix = '8kuw66xel/rudy_2.jpg'
	if randNum == 2:
		picSuffix = 'htx2gb6al/rudy_3.jpg'
	if randNum == 3:
		picSuffix = 'uzckmf065/rudy_4.jpg'
	if randNum == 4:
		picSuffix = 'nkn8u1eal/rudy_5.jpg'
	if randNum == 5:
		picSuffix = 'wgy0xz4wt/rudy_6.jpg'
	if randNum == 6:
		picSuffix = 'hm9fjsvbx/rudy_7.jpg'
	if randNum == 7:
		picSuffix = 'gy0l0uwm5/rudy_8.jpg'
	if randNum == 8:
		picSuffix = '4knqty6xp/rudy_9.jpg'
	if randNum == 9:
		picSuffix = 'otfptevml/rudy_10.jpg'
	if randNum == 10:
		picSuffix = 'b11axs4v1/rudy_11.jpg'
	if randNum == 11:
		picSuffix = 's2u4zvjq5/rudy_12.jpg'
	if randNum == 12:
		picSuffix = 'iwbuclehp/rudy_13.jpg'
	if randNum == 13:
		picSuffix = 'mtz4201b1/rudy_14.jpg'
	if randNum == 14:
		picSuffix = 'biwgdmufx/rudy_15.jpg'
	if randNum == 15:
		picSuffix = 'b7f00vdzx/rudy_16.jpg'
	if randNum == 16:
		picSuffix = 'aj65hxfa5/rudy_17.jpg'
	if randNum == 17:
		picSuffix = 'vhcbg0f4t/rudy_18.jpg'
	if randNum == 18:
		picSuffix = 'euur6xm71/rudy_19.jpg'
	if randNum == 19:
		picSuffix = 'ismma2ye5/rudy_20.jpg'
	if randNum == 20:
		picSuffix = 'fzteq1y1p/rudy_21.jpg'
	if randNum == 21:
		picSuffix = 'acx1skvj1/rudy_22.jpg'
	if randNum == 22:
		picSuffix = 'yup5ggy3h/rudy_23.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### Post Carley Pic ###############

def PostCarleyPic():
	randNum = random.randrange(0, 14)
	sNum = '20'

	if randNum == 0:
		picSuffix = '5lx6ak2ot/carley_1.jpg'
	if randNum == 1:
		picSuffix = '485jf93fh/carley_2.jpg'
	if randNum == 2:
		picSuffix = '7gem61f31/carley_3.jpg'
	if randNum == 3:
		picSuffix = 'nsonvrtel/carley_4.jpg'
	if randNum == 4:
		picSuffix = 'y410ofl3x/carley_5.jpg'
	if randNum == 5:
		picSuffix = 'huauljafx/carley_6.jpg'
	if randNum == 6:
		picSuffix = 'ixuyxhv31/carley_7.jpg'
	if randNum == 7:
		picSuffix = 'jonp39xgd/carley_8.jpg'
	if randNum == 8:
		picSuffix = '9fv7xg9el/carley_9.jpg'
	if randNum == 9:
		picSuffix = '9h55qvb8d/carley_10.jpg'
	if randNum == 10:
		picSuffix = 'vhli7htwd/carley_11.jpg'
	if randNum == 11:
		picSuffix = 'mb37k7onx/carley_12.jpg'
	if randNum == 12:
		picSuffix = 'u58ejclul/carley_13.jpg'
	if randNum == 13:
		picSuffix = 'dvi8ggb6l/carley_14.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### Post Bambi Pic ###############	

def PostBambiPic():
	randNum = random.randrange(0, 21)
	sNum = '20'

	if randNum == 0:
		picSuffix = 's37x53nvh/bambi_1.jpg'
	if randNum == 1:
		picSuffix = 'pn63r95st/bambi_2.jpg'
	if randNum == 2:
		picSuffix = 'sij6y49st/bambi_3.jpg'
	if randNum == 3:
		picSuffix = '5icjlsbz1/bambi_4.jpg'
	if randNum == 4:
		picSuffix = 'gvz2wzmhp/bambi_5.jpg'
	if randNum == 5:
		picSuffix = '8ezkm2hst/bambi_6.jpg'
	if randNum == 6:
		picSuffix = '5m6d21hgd/bambi_7.jpg'
	if randNum == 7:
		picSuffix = 'xnkefqmql/bambi_8.jpg'
	if randNum == 8:
		picSuffix = 'fyx91v0d9/bambi_9.jpg'
	if randNum == 9:
		picSuffix = 'divfo0ial/bambi_10.jpg'
	if randNum == 10:
		picSuffix = 'b2tma607x/bambi_11.jpg'
	if randNum == 11:
		picSuffix = '4dn2u5evx/bambi_12.jpg'
	if randNum == 12:
		picSuffix = 'wrsie12fx/bambi_13.jpg'
	if randNum == 13:
		picSuffix = '5ih4zj1ct/bambi_14.jpg'
	if randNum == 14:
		picSuffix = 'erjb9na8t/bambi_15.jpg'
	if randNum == 15:
		picSuffix = 's9q7lxme5/bambi_16.jpg'
	if randNum == 16:
		picSuffix = '3uhzkvnh9/bambi_17.jpg'
	if randNum == 17:
		picSuffix = '6pv2rqrh9/bambi_18.jpg'
	if randNum == 18:
		picSuffix = 'aavjoplel/bambi_19.jpg'
	if randNum == 19:
		picSuffix = 'v91pmsl99/bambi_20.jpg'
	if randNum == 20:
		picSuffix = 'rdybk823h/bambi_21.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### Post Nick Pic ###############	

def PostNickPic():
	randNum = random.randrange(0, 20)
	sNum = '20'

	if randNum == 0:
		picSuffix = '65kn2snml/nick_1.jpg'
	if randNum == 1:
		picSuffix = 'a37ws7afx/nick_2.jpg'
	if randNum == 2:
		picSuffix = 'uomok3s0t/nick_3.jpg'
	if randNum == 3:
		picSuffix = 'pehpst7rx/nick_4.jpg'
	if randNum == 4:
		picSuffix = '7ppz16w0t/nick_5.jpg'
	if randNum == 5:
		picSuffix = 'np8mkqs2l/nick_6.jpg'
	if randNum == 6:
		picSuffix = 'xntl781i5/nick_7.jpg'
	if randNum == 7:
		picSuffix = 'wmxxvu9wd/nick_8.jpg'
	if randNum == 8:
		picSuffix = 'ovh7xa5r1/nick_9.jpg'
	if randNum == 9:
		picSuffix = '4cmbs7rtp/nick_10.jpg'
	if randNum == 10:
		picSuffix = 'nizive8bh/nick_11.jpg'
	if randNum == 11:
		picSuffix = 'ywm26liu5/nick_12.jpg'
	if randNum == 12:
		picSuffix = 'tz8hlhgv1/nick_13.jpg'
	if randNum == 13:
		picSuffix = '5wrnqm07x/nick_14.jpg'
	if randNum == 14:
		picSuffix = 'vtlc383vh/nick_15.jpg'
	if randNum == 15:
		picSuffix = 'baqfy5py5/nick_16.jpg'
	if randNum == 16:
		picSuffix = 'kjsm89yu5/nick_17.jpg'
	if randNum == 17:
		picSuffix = 'tg7zpyeu5/nick_18.jpg'
	if randNum == 18:
		picSuffix = 'uwji83hr1/nick_19.jpg'
	if randNum == 19:
		picSuffix = '4cqx5yh7h/nick_20.jpg'

	return 'https://s' + sNum + '.postimg.org/' + picSuffix

############### Post Calvin Pic ###############

def PostCalvinPic():
	return 'https://s20.postimg.org/a275q9ndp/calvin.jpg'

############### Post Monica Pic ###############

def PostMonicaPic():
	return 'https://s20.postimg.org/h6oyzaun1/monica.png'

############### People Pics ###############

def PeoplePics(wordList):
	# Return list of urls to post
	returnURLS = []

	# Switches so we only post one pic per person
	joePosted 		= "false"
	mariaPosted 	= "false"
	tyreePosted 	= "false"
	alexisPosted 	= "false"
	rudyPosted 		= "false"
	carleyPosted	= "false"
	bambiPosted		= "false"
	nickPosted 		= "false"
	calvinPosted 	= "false"
	monicaPosted	= "false"

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

		# Alexis
		if word == "alexis" and alexisPosted == "false":
			alexisPosted = "true"
			returnURLS.append(PostAlexisPic())

		# Rudy
		if (word == "rudy" or word == "wudy") and rudyPosted == "false":
			rudyPosted = "true"
			returnURLS.append(PostRudyPic())

		# Carley
		if (word == "carley" or word == "carl") and carleyPosted == "false":
			carleyPosted = "true"
			returnURLS.append(PostCarleyPic())

		# Bambi
		if (word == "bambi" or word == "brandt") and bambiPosted == "false":
			bambiPosted = "true"
			returnURLS.append(PostBambiPic())

		# Nick
		if (word == "nick" or word == "nicolas") and nickPosted == "false":
			nickPosted = "true"
			returnURLS.append(PostNickPic())

		# Calvin
		if (word == "calvin" or word == "cal") and calvinPosted == "false":
			calvinPosted = "true"
			returnURLS.append(PostCalvinPic())
		
		# Mah Nicca
		if (word == "monica" or word == "nicca" or word == "nigga") and monicaPosted == "false":
			monicaPosted = "true"
			returnURLS.append(PostMonicaPic())

	return returnURLS
