# privacy_django

command  

$ mkdir django_app  

$ cd django_app  

$ virtualenv venv  

$ venv\Scripts\activate  

$ pip install --upgrade pip  

$ pip install django  

$ pip install dj-database-url gunicorn whitenoise  

$ pip freeze > requirements.txt  

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

$ pip install -U nltk  

$ import nltk, re  

$ from nltk import word_tokenize  

$ tokens = word_tokenize(raw)  

$ tg=nltk.pos_tag(tokens, tagset='universal')  

$ tag_fd = nltk.FreqDist(tag for (word, tag) in tg)  

$ tag_fd.most_common()  

$ re.findall(r'\w+|\S\w*', raw)  

$ aa=re.findall(r'\b([a-zA-Z]+)\b', raw)  

$ for s in stops:  
	while s in aa: aa.remove(s)  

$ [porter.stem(t) for t in aa]  

$ [lancaster.stem(t) for t in aa]  

$ [wnl.lemmatize(t) for t in aa]  

$ for d in ddp:  
	for r in rr:  
		if d==r:  
			print(d)  

$ from nltk.parse.stanford import StanfordDependencyParser  
$ dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")  









$ financial = ['anz', 'asb', 'bnz', 'kiwi', 'bank', 'kiwibank', 'westpac', 'account', 'no.', 'account', 'number', 'american', 'express', 'amount', 'asset', 'bank', 'bank', 'account', 'no.', 'bank', 'account', 'number', 'budget', 'cost', 'credit', 'credit', 'card', 'credit', 'card', 'no.', 'credit', 'card', 'number', 'currency', 'debit', 'deposit', 'deposit', 'amount', 'dollar', 'estate', 'expense', 'gain', 'home', 'loan', 'homeloan', 'income', 'interest', 'rate', 'invest', 'kiwi', 'saver', 'loss', 'master', 'card', 'million', 'overdue', 'overdue', 'amount', 'payment', 'payment', 'amount', 'price', 'spend', 'value', 'visa', 'wealth', 'wealthy']  

$ cyber = ['ddos', 'botnet', 'brute', 'force', 'cain', 'and', 'abel', 'conficker', 'cyber', 'attack', 'cyber', 'security', 'cyber', 'terror', 'dedicated', 'denial', 'of', 'service', 'denial', 'of', 'service', 'email', 'email', 'address', 'hacker', 'keylogger', 'malware', 'mysql', 'injection', 'pass', 'code', 'passcode', 'password', 'password', 'phish', 'phreak', 'pin', 'code', 'pin', 'no.', 'pin', 'number', 'ps', 'rootkit', 'scam', 'sign', 'in', 'sign', 'out', 'spam', 'trojan', 'user', 'user', 'id', 'user', 'name', 'virus', 'worm']  

$ stops = ['a’s', 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', 'ain’t', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', 'aren’t', 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c’mon', 'c’s', 'came', 'can', 'can’t', 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'couldn’t', 'course', 'currently', 'definitely', 'described', 'despite', 'did', 'didn’t', 'different', 'do', 'does', 'doesn’t', 'doing', 'don’t', 'done', 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadn’t', 'happens', 'hardly', 'has', 'hasn’t', 'have', 'haven’t', 'having', 'he', 'he’s', 'hello', 'help', 'hence', 'her', 'here', 'here’s', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i’d', 'i’ll', 'i’m', 'i’ve', 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', 'isn’t', 'it', 'it’d', 'it’ll', 'it’s', 'its', 'itself', 'just', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'let’s', 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', 'shouldn’t', 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't’s', 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'that’s', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'there’s', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', 'they’d', 'they’ll', 'they’re', 'they’ve', 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', 'wasn’t', 'way', 'we', 'we’d', 'we’ll', 'we’re', 'we’ve', 'welcome', 'well', 'went', 'were', 'weren’t', 'what', 'what’s', 'whatever', 'when', 'whence', 'whenever', 'where', 'where’s', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'who’s', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'won’t', 'wonder', 'would', 'would', 'wouldn’t', 'yes', 'yet', 'you', 'you’d', 'you’ll', 'you’re', 'you’ve', 'your', 'yours', 'yourself', 'yourselves', 'zero']  
