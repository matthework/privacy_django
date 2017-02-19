import io, re, nltk, ntpath, PyPDF2, docx
from nltk import word_tokenize
from urllib import request, error
from bs4 import BeautifulSoup
from nltk.parse.stanford import StanfordDependencyParser
import time
# import threading
# import multiprocessing
from multiprocessing import Pool

nltk.data.path.append('./nltk_data/')


def doWeb(kws, url):
	result = ''
	title = ''
	if url[0:4] == 'eg: ':
		url = url[4:]
	if url[0] == ':':
		url = url[1:]
	if url[0:4] != 'http':
		url = 'http://' + url
	if url[-4:] == '.pdf':
		result = 'Please use Document page for a PDF file!'
	elif url[-5:] == '.docx' or url[-4:] == '.doc':
		result = 'Please use Document page for a Word file!'
	elif url[-4:] == '.txt':
		result = 'Please use Document page for a Txt file!'
	else:
		print('url2: ' + url)
		try:
			html = request.urlopen(url).read().decode('utf8')
			raw = BeautifulSoup(html, 'html.parser').body.get_text()
			title = BeautifulSoup(html, 'html.parser').title.string
			result = processRaw(kws, raw)
		except Exception as e:
			print(e)
			result = 'Exception: ' + str(e)

	return '<strong>' + title + '<br>(' + url + ')</strong><br><br>' + result


def doDoc(kws, path):
	result = ''
	raw = ''
	name = ntpath.basename(path)
	if path[0:5] == 'web: ':
		path = path[5:]
	if path[0:7] == 'local: ':
		path = path[7:]
	if path[0] == ':':
		path = path[1:]
	if path[1:3] != ':\\' and path[0:4] != 'http':
		path = 'http://' + path
	print('path2: ' + path)
	
	try:
		# txt file
		if '.' in name and name.split('.')[1].lower() == 'txt':
			if path[1:3] == ':\\':
				path = 'file:///' + path
			print('txt: ' + path)
			raw = request.urlopen(path).read().decode('utf8')
			result = processRaw(kws, raw)
		
		# tpdf file
		elif '.' in name and name.split('.')[1].lower() == 'pdf':
			if path[1:3] == ':\\':
				path = 'file:///' + path
			print('pdf: ' + path)

			# pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
			remote_file = request.urlopen(path).read()
			memory_file = io.BytesIO(remote_file)

			pdfReader = PyPDF2.PdfFileReader(memory_file)
			pnums = pdfReader.getNumPages()
			if pnums>3:
				pnums = 3

			for i in range(pnums):
				raw += pdfReader.getPage(i).extractText()
			result = processRaw(kws, raw)
		
		# docx file
		elif '.' in name and name.split('.')[1].lower() == 'docx':
			# if path[1:3] == ':\\':
			# 	path = 'file:///' + path
			print('docx: ' + path)
			# remote_file = request.urlopen(path).read()
			# memory_file = io.BytesIO(remote_file).getvalue()
			# print(memory_file.decode('utf8'))
			# print(str(memory_file,'utf-8'))

			doc = docx.Document(path)
			fullText = []
			for para in doc.paragraphs:
				fullText.append(para.text)
			raw = '\n'.join(fullText)
			result = processRaw(kws, raw)

		else:
			result = 'Please use Web for webpage processing!'
	
	except Exception as e:
		print(e)
		result = 'Exception: ' + str(e)

	return '<strong>' + name + '<br>(' + path + ')</strong><br><br>' + result


def processRaw(kws, raw):
	# # kws = ["prove", "identity", "approval", "gain", "allowed", "password", "passwords", "username", "authentication", "access", "code" , "secret"]
	# kws = ["cost", "cyber-crime", "estimated", "$", "445", "billion", "266", "cyber-espionage", "stealing", "individuals", "information", "believed", "800", "million", "people", "financial-losses", "cyber-theft", "cause", "150,000", "europeans", "lose", "jobs", "report", "conducted", "internet-security", "company-mcafee", "damages", "trade", "nations", "competitiveness", "innovation", "growth", "slows", "pace", "mcafee", "calling", "governments", "begin", "effort", "collect", "publish", "data", "help", "countries", "companies", "make", "choices", "risk" , "policy"]
	# if raw:
	# 	tokens = word_tokenize(raw)
	# 	print(len(tokens))
	# 	kwords = []
	# 	for k in kws:
	# 		# kwords.append(k.name.lower())
	# 		kwords.append(k.lower())

	# 	text = []
	# 	for s in tokens:
	# 		if(s.lower() in kwords):
	# 			tts = "<input onclick='responsiveVoice.speak(\\\"" + s + "\\\");' type='button' value='🔊 xxxxx' />"
	# 			text.append(tts) 
	# 		else:
	# 			text.append(s)
	# 	result = ' '.join(text)
	# else:
	# 	result = 'The url is invalid or the file is not found!'

	
	# out = {}
	# sen1 = """The cost of cyber-crime for the global economy has been estimated at $445 billion ( 266 billion) annually."""
	# sen2 = """Cyber-espionage and stealing individuals' personal information is believed to have affected more than 800 million people during 2013."""


	# process_a = multiprocessing.Process(target=getDependency(dep_parser,sen1))
	# process_b = multiprocessing.Process(target=getDependency(dep_parser,sen2))

	# process_b.start()
	# process_a.start()


	# process_a.join
	# process_b.join

	# a_thread = threading.Thread(target=getDependency(dep_parser,sen1))
	# a_thread.start()

	# b_thread = threading.Thread(target=getDependency(dep_parser,sen2))
	# b_thread.start()

	# a_thread.join()
	# b_thread.join()

	# uds1 = [list(parse.triples()) for parse in dep_parser.raw_parse(sen1)]
	# uds2 = [list(parse.triples()) for parse in dep_parser.raw_parse(sen2)]

	senlist = raw.split('. ')
	# for index, s in enumerate(senlist):
	# 	print('('+ str(index) + ')' +s)

	start = time.time()

	results = Pool().map(getDependency, senlist)

	print(results)

	# uds = [list(parse.triples()) for parse in dep_parser.raw_parse(raw)]
	end = time.time()
	print('Processing time: ' + str(end-start))
	# print(uds)
	tokens = word_tokenize(raw)
	print(len(tokens))
	result = 'done!'
	return result + '<br><br><br><br><br><br>'


def getDependency(sen):
	dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
	uds = [list(parse.triples()) for parse in dep_parser.raw_parse(sen)]
	return str(uds)

def sortKey(kws, cats):
	result = {}
	for c in cats:
		result[c] = []
		for k in kws:
			if k.category == c:
				result[c].append(k.name.lower())

	return result


def testRaw(raw, stops):

	# tokens = word_tokenize(raw)
	ww = re.findall(r'\b([a-zA-Z]+)\b', raw)
	words = [w.lower() for w in ww]
	print(words)

	list1 = words
	for s in stops:
		while s in list1 : list1.remove(s)
	
	# remove digits and punctuation

	print(list1)

















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