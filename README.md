# privacy_django (master project by matt wang 2017)

Requirements:

Python 3.5.1 (the major programming language for this project)  
Django 1.10.5 (the web development framework)  
NLTK 3.2.2 (the natural language toolkit)  
Beautifulsoup4 4.5.3 (the CSS styling library for web application)  
dj-database-url 0.4.2 (the library managing the database in Django)  
PyPDF2 1.26.0 (the library used for extracting texts from pdf file)  
python-docx 0.8.6 (the library used for extracting texts from docx file)  
ResponseVoice 1.4.0 (the text-to-speech library)   
Java SDK (JVM for stanford parser)

pip install -U django  
pip install -U nltk  
pip install -U bs4  
pip install -U PyPDF2  
pip install -U python-docx  
pip install -U whitenoise  

pip freeze > requirements.txt  

open idle  
import nltk  
nltk.download()  
download 'tokenizers' to C:\nltk_data  
download 'stanford-parser-full-2016-10-31.zip' from standford website, then unzip it  
copy 'stanford-parser.jar' and 'stanford-parser-3.7.0-models.jar' to C:\nltk_data\stanford-parser  
set the CLASSPATH='C:\nltk_data\stanford-parser'
copy 'dependencygraph.py' to '\Python35\Lib\site-packages\nltk\parse' and replace original one


Commands:   

$ mkdir django_app  
$ cd django_app  
$ virtualenv venv  
$ venv\Scripts\activate  
$ pip install --upgrade pip  
$ pip install dj-database-url gunicorn whitenoise  
$ pip freeze > requirements.txt  
$ pip install -r requirements.txt  
$ django-admin.py startproject mysite .  
$ python manage.py migrate  
$ python manage.py runserver  
$ python manage.py startapp privacy  
$ python manage.py makemigrations privacy  
$ python manage.py migrate privacy  
$ python manage.py createsuperuser  
$ heroku login  
$ heroku apps  
$ heroku run --app privacy-django python manage.py migrate  
$ heroku run --app privacy-django python manage.py createsuperuser   
$ import nltk, re  
$ from nltk import word_tokenize  
$ tokens = word_tokenize(raw)  
$ from nltk.corpus import wordnet as wn  
$ tg=nltk.pos_tag(tokens, tagset='universal')  
$ tag_fd = nltk.FreqDist(tag for (word, tag) in tg)  
$ tag_fd.most_common()  
$ re.findall(r'\w+|\S\w*', raw)  
$ aa=re.findall(r'\b([a-zA-Z]+)\b', raw)  
$ porter = nltk.PorterStemmer()  
$ [porter.stem(t) for t in aa]  
$ [lancaster.stem(t) for t in aa]  
$ [wnl.lemmatize(t) for t in aa]  
$ from nltk.parse.stanford import StanfordDependencyParser  
$ dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")  
$ [list(parse.triples()) for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")]  
$ pip install pexpect  
$ pip install unidecode  
$ pip install jsonrpclib  
$ pip install jsonrpclib-pelix  