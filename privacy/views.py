from django.shortcuts import render
from .models import Keyword, Category
from .mycode import doWeb, doDoc, sortKey


def main(request):
    kws = Keyword.objects.order_by('name')	
    context = {'kws': kws}
    return render(request, 'privacy/main.html', context)

def web(request):
	kws = Keyword.objects.order_by('name')
	url = ''
	out = ''
	if request.GET.get('gobtn'):
		url = request.GET.get('url')
		print('url1: ' + url)
		out = '<strong>Result: </strong><br><br>' + doWeb(kws, url)
	context = {'kws': kws, 'out': out}
	return render(request, 'privacy/web.html', context)

def doc(request):
	kws = Keyword.objects.order_by('name')
	path = ''
	out = ''
	if request.GET.get('filebtn'):
		path = request.GET.get('doc')
		print('path1: ' + path)
		out = '<strong>Result: </strong><br><br>' + doDoc(kws, path)
	context = {'kws': kws, 'out': out}
	return render(request, 'privacy/doc.html', context)

def keyword(request):
	kws = Keyword.objects.order_by('name')
	cats = Category.objects.order_by('name')
	sortkeys = {}
	sortkeys = sortKey(kws, cats)
	# print(sortkeys)
	context = {'kws': kws, 'cats': cats, 'sortkeys': sortkeys}
	return render(request, 'privacy/keyword.html', context)

def about(request):
    return render(request, 'privacy/about.html')