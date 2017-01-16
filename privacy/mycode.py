import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup


def doWeb(kws, url):
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html, 'html.parser').body.get_text()
	tokens = word_tokenize(raw)
	kwords = []
	for k in kws:
		kwords.append(k.name.lower())

	text = []
	for s in tokens:
		if(s.lower() in kwords):
			tts = "<input onclick='responsiveVoice.speak(\\\"" + s + "\\\");' type='button' value='🔊 xxxxx' />"
			text.append(tts) 
		else:
			text.append(s)
	result = ' '.join(text)
	return '<strong>Result: </strong><br><br>' + result + '<br><br><br><br><br><br>'

	# body = BeautifulSoup(html, 'html.parser').body
	# kwords = []
	# for k in kws:
	# 	kwords.append(k.name.lower())
	# for kw in kwords:
	# 	if kw in body:
	# 		tts = "<input onclick='responsiveVoice.speak(\\\"" + kws + "\\\");' type='button' value='🔊 xxxxx' />"
	# 		body.replace(kw, tts)
	# result = body.prettify()
	# print(result)
	# return result