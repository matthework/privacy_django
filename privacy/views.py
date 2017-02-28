from django.shortcuts import render
from .models import Keyword, Category
from .mycode import doWeb, doDoc, sortKey, testRaw, searchWN
import time


def main(request):
    kset = Keyword.objects.order_by('name')	
    context = {'kset': kset}
    return render(request, 'privacy/main.html', context)

def web(request):
	kset = Keyword.objects.order_by('name')
	cats = Category.objects.order_by('name')
	cats_user = []
	url = ''
	out = ''
	if request.GET.get('gobtn'):
		cats_user = request.GET.getlist('checks')
		print('cats_user: ' + str(cats_user))
		kws = []
		for k in kset:
			if k.category.name in cats_user:
				kws.append(k.name.lower())
				# print(kws)
		url = request.GET.get('url')
		print('url1: ' + url)
		out = '<strong>Result: </strong><br><br>' + doWeb(kws, url)
	context = {'cats': cats, 'out': out}
	return render(request, 'privacy/web.html', context)

def doc(request):
	kset = Keyword.objects.order_by('name')
	cats = Category.objects.order_by('name')
	cats_user = []
	path = ''
	out = ''
	if request.GET.get('filebtn'):
		cats_user = request.GET.getlist('checks')
		print('cats_user: ' + str(cats_user))
		kws = []
		for k in kset:
			if k.category.name in cats_user:
				kws.append(k.name.lower())
				# print(kws)
		path = request.GET.get('doc')
		print('path1: ' + path)
		out = '<strong>Result: </strong><br><br>' + doDoc(kws, path)
	context = {'cats': cats, 'out': out}
	return render(request, 'privacy/doc.html', context)

def kws(request):
	kset = Keyword.objects.order_by('name')
	cats = Category.objects.order_by('name')
	sortkeys = {}
	sortkeys = sortKey(kset, cats)
	# print(sortkeys)
	context = {'kset': kset, 'cats': cats, 'sortkeys': sortkeys}
	return render(request, 'privacy/kws.html', context)

def wordnet(request, kword, category):
	synsets = searchWN(kword)
	synonyms = []
	if request.GET.get('wnbtn'):
		synonyms = request.GET.getlist('checks[]')
		synonyms = list(set(synonyms))
		# print(synonyms)
	context = {'word': kword.upper(), 'category': category, 'synsets': synsets, 'synonyms':synonyms}
	return render(request, 'privacy/wn.html', context)

def about(request):
    return render(request, 'privacy/about.html')