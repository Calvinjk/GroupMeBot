import re

def Harambe(message):
	if 'harambe' in message:
		return "DICKS OUT"
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