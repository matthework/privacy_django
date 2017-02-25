import io, re, nltk, ntpath, PyPDF2, docx
from nltk import word_tokenize
from urllib import request, error
from bs4 import BeautifulSoup
from nltk.parse.stanford import StanfordDependencyParser
import time
from multiprocessing import Pool
from nltk.corpus import stopwords


nltk.data.path.append('./nltk_data/')


def doWeb(kset, url):
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
			result = processRaw(kset, raw)
		except Exception as e:
			print(e)
			result = 'Exception: ' + str(e)

	return '<strong>' + title + '<br>(' + url + ')</strong><br><br>' + result


def doDoc(kset, path):
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
			result = processRaw(kset, raw)
		
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
			result = processRaw(kset, raw)
		
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
			result = processRaw(kset, raw)

		else:
			result = 'Please use Web for webpage processing!'
	
	except Exception as e:
		print(e)
		result = 'Exception: ' + str(e)

	return '<strong>' + name + '<br>(' + path + ')</strong><br><br>' + result


def processRaw(kset, raw):
	result = ""
	# second = 0.2

	cats = ['financial','cyber']
	kws = []
	for k in kset:
		if k.category.name in cats:
			kws.append(k.name.lower())
	# print(kws)

	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sen_list = sent_detector.tokenize(raw.strip())
	sen_list = list(filter(None, sen_list))
	# print(sen_list)

	pss_input = []
	pss_list = []
	for index, sen in enumerate(sen_list):
		if len(sen)>0:
			k = searchKWS(sen, kws)
			if k['hasKWS']:
				pss_input.append([sen, k['kws_index']])
				pss_list.append(index)


	print(pss_input)
	print(pss_list)


	# uds_list = getDependency(raw)
	# uds_list = Pool().map(getDependency, sen_list)
	# print(uds_list)

	out_list = []
	if len(pss_input)>0:
		start = time.time()
		out_list = Pool().map(identityPSD, pss_input)
		end = time.time()
		t = end-start
		print('Processing Time: ' + str(t))
	else:
		result = raw


	output = []
	index_out = 0
	for i, s in enumerate(sen_list):
		if len(out_list)>0 and i in pss_list:
			output.append(out_list[index_out])
			index_out +=1
		else:
			output.append(s)

	result = ' '.join(output)

	tokens = word_tokenize(raw)
	print(len(tokens))

	return result + '<br><br><br><br><br><br>'



def searchKWS(sen, kws):
	hasKWS = False
	kws_index = []
	tokens = [t.lower() for t in word_tokenize(sen)]

	## round 1
	s = ""
	for kw in kws:
		if kw in sen.lower():
			s += kw + ' '

	list1 = s.split(' ')
	# print(list1)
	for i, s in enumerate(tokens):
		if s.lower() in list1:
			kws_index.append(i)


	## round 2
	porter = nltk.PorterStemmer()
	stem_tokens = [porter.stem(t) for t in tokens]  

	stem_kws = [porter.stem(kw) for kw in kws]
	# print(stem_kws) 


	for i, sk in enumerate(stem_tokens):  
		for st in stem_kws:  
			if sk==st:  
				kws_index.append(i)


	## print all keywrods found
	# for i, s in enumerate(tokens):
	# 	if i in kws_index:
	# 		print(s)

	kws_index = list(set(kws_index))
	if len(kws_index)>0:
		hasKWS = True		
		# print(kws_index)

	output = {"hasKWS": hasKWS, "kws_index": kws_index}
	return output



def identityPSD(input):
	result = "" 
	sen = input[0]
	kws_index = input[1]
	uds = getDependency(sen)
	# print(uds)

	psd_list = coverPSD(uds, kws_index)
	sd_list = list(set(kws_index + psd_list))
	# print(sd_list)
	text = []
	tokens = word_tokenize(sen)
	for i, s in enumerate(tokens):
		if i in sd_list:
			print(s)
			tts = "<input onclick='responsiveVoice.speak(\\\"" + s + "\\\");' type='button' value='🔊 xxxxx' />"
			text.append(tts) 
		else:
			text.append(s)
	result = ' '.join(text)

	return result



def getDependency(sen):
	dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
	uds = [list(parse.triples()) for parse in dep_parser.raw_parse(sen)]
	# for parse in dep_parser.raw_parse(sen):
	# 	print(parse)
	for u in uds[0]:
		print(u)
	return uds



def coverPSD(uds, kws_index):
	output = ""
	# pw = []
	psd = []
	noun = ['NN', 'NNS', 'NNP', 'NNPS']
	verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
	number = ['CD']
	re1 = ['compound', 'nmod', 'conj']
	re2 = ['nummod']
	re3 = ['compound']
	re4 = ['nsubj', 'dobj' ,'nmod', 'nsubjpass']
	re5 = ['xcomp', 'ccomp', 'conj']
	for u in uds[0]:
		if u[0][2]-1 in kws_index:
			if u[0][1] in noun and u[2][1] in noun and u[1] in re1:
				psd.append(u[2][2]-1)
				# pw.append(u[2][0])
			if u[0][1] in noun and u[2][1] in number and u[1] in re2:
				psd.append(u[2][2]-1)
			if u[0][1] in number and u[2][1] in number and u[1] in re3:
				psd.append(u[2][2]-1)
				# pw.append(u[2][0])
			if u[0][1] in verb and u[2][1] in noun and u[1] in re4:
				psd.append(u[2][2]-1)
				# pw.append(u[2][0])
			if u[0][1] in verb and u[2][1] in verb and u[1] in re5:
				psd.append(u[2][2]-1)
				# pw.append(u[2][0])
				coverPSD(uds, [u[2][2]-1])

		if u[2][2]-1 in kws_index:
			if u[0][1] in noun and u[2][1] in noun and u[1] in re1:
				psd.append(u[0][2]-1)
			if u[0][1] in noun and u[2][1] in number and u[1] in re2:
				psd.append(u[0][2]-1)
			if u[0][1] in number and u[2][1] in number and u[1] in re3:
				psd.append(u[0][2]-1)

	# print(pw)
	return psd



def sortKey(kset, cats):
	result = {}
	for c in cats:
		result[c] = []
		for k in kset:
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




# def triples(node = None):
# 	print("triples")

#     if not node:
#         node = parse.root

#     head = (node['word'], node['ctag'], node['address'])
#     for i in sorted(chain.from_iterable(node['deps'].values())):
#         dep = parse.get_by_address(i)
#         yield (head, dep['rel'], (dep['word'], dep['ctag'], node['address']))
#         for triple in triples(dep):
#             yield triple












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