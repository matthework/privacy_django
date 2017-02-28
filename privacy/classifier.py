import nltk, re
from nltk.classify import SklearnClassifier
# from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.svm import SVC
import ast
from os import listdir
from random import randint


## extract features from documents
def featureExtractor(raw): 
	fvector = {}
	# tokens = word_tokenize(raw.strip())
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(raw.strip())
	# stops = set(stopwords.words('english'))
	# for s in stops:  
	# 	while s in tokens: tokens.remove(s)  

	fdist = nltk.FreqDist(tokens)
	top = fdist.most_common(200)
	# print(top)
	for t in top:
		fvector[t[0]] = t[1]

	print(fvector)


	return fvector


## train training documents
def trainData():

	tdata = []
	categories = listdir('data/train')
	print(categories)

	for c in categories:
		tup = ()
		text = ''
		fnames = listdir('data/train/'+ c)
		for f in fnames:
			path = 'data/train/' + c + '/'+ f
			with open(path, 'r') as myfile3:
				raw = myfile3.read().replace('\n', '')
				text += raw
		
		tup = (featureExtractor(text), c)
		tdata.append(tup)

	# print(tdata)
	return tdata


## load trained data
def getTrainData(path):

	train_file = path
	with open(train_file, 'r') as myfile1:
		raw_train=myfile1.read().replace('\n', '')
	# print(raw_train)
	train_data = ast.literal_eval(raw_train)

	return train_data


## predict a category for new document
def predict(path, classif):
	test_file = path
	with open(test_file, 'r') as myfile2:
		raw_test=myfile2.read().replace('\n', '')

	# print(raw_test)
	test_data = featureExtractor(raw_test)

	result = classif.classify(test_data)

	return result




if __name__ == "__main__":
    
    result = ''

    ## training
    train_file = 'data/train_data.txt'
    # train_file = 'data/train_data1.txt'
    # train_data = trainData(train_file)
    train_data = getTrainData(train_file)

    ## classifying
    test_file = 'data/test.txt'
    # test_file = 'data/test1.txt'
    classif = SklearnClassifier(SVC(), sparse=False).train(train_data)
    result = predict(test_file, classif)

    print(result)