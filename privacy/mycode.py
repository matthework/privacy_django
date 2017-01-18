import io, nltk, ntpath, PyPDF2, docx
from nltk import word_tokenize
from urllib import request, error
from bs4 import BeautifulSoup

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
		except error.URLError as e:
			print(e.reason)
			result = 'The url is invalid or the webpage is not found!'
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
			try:
				doc = docx.Document(path)
				fullText = []
				for para in doc.paragraphs:
					fullText.append(para.text)
				raw = '\n'.join(fullText)
			except Exception as e:
				print(e)
				result = 'The url is invalid or the file is not found!'

			result = processRaw(kws, raw)

		else:
			result = 'The url is invalid or the file is not found!'
	
	except error.URLError as e:
		print(e.reason)
		result = 'The url is invalid or the file is not found!'

	return '<strong>' + name + '<br>(' + path + ')</strong><br><br>' + result


def processRaw(kws, raw):
	if raw:
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
	else:
		result = 'The url is invalid or the file is not found!'
	return result + '<br><br><br><br><br><br>'






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