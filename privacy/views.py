from django.shortcuts import render
from .models import Keyword, Category
from .mycode import doWeb, doDoc, sortKey, testRaw
import time


def main(request):
    kset = Keyword.objects.order_by('name')	
    context = {'kset': kset}
    return render(request, 'privacy/main.html', context)

def web(request):
	kset = Keyword.objects.order_by('name')
	url = ''
	out = ''
	if request.GET.get('gobtn'):
		url = request.GET.get('url')
		print('url1: ' + url)
		out = '<strong>Result: </strong><br><br>' + doWeb(kset, url)
	context = {'kset': kset, 'out': out}
	return render(request, 'privacy/web.html', context)

def doc(request):
	kset = Keyword.objects.order_by('name')
	path = ''
	out = ''
	if request.GET.get('filebtn'):
		path = request.GET.get('doc')
		print('path1: ' + path)
		out = '<strong>Result: </strong><br><br>' + doDoc(kset, path)
	context = {'kset': kset, 'out': out}
	return render(request, 'privacy/doc.html', context)

def keyword(request):
	kset = Keyword.objects.order_by('name')
	cats = Category.objects.order_by('name')
	sortkeys = {}
	sortkeys = sortKey(kset, cats)
	# print(sortkeys)
	context = {'kset': kset, 'cats': cats, 'sortkeys': sortkeys}
	return render(request, 'privacy/keyword.html', context)

def kw(request):
	word = 'bank'
	context = {'word': word}
	return render(request, 'privacy/kw.html', context)

def about(request):
    return render(request, 'privacy/about.html')