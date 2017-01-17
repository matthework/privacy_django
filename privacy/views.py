from django.shortcuts import render
from .models import Keyword
from .mycode import doWeb, doDoc


def main(request):
    kws = Keyword.objects.order_by('created_date')	
    context = {'kws': kws}
    return render(request, 'privacy/main.html', context)

def web(request):
	kws = Keyword.objects.order_by('created_date')
	url = ''
	out = ''
	if request.GET.get('gobtn'):
		url = request.GET.get('url')
		print('url1: ' + url)
		out = '<strong>Result: </strong><br><br>' + doWeb(kws, url)
	context = {'kws': kws, 'out': out}
	return render(request, 'privacy/web.html', context)

def doc(request):
	kws = Keyword.objects.order_by('created_date')
	path = ''
	out = ''
	if request.GET.get('filebtn'):
		path = request.GET.get('doc')
		print('path1: ' + path)
		out = '<strong>Result: </strong><br><br>' + doDoc(kws, path)
	context = {'kws': kws, 'out': out}
	return render(request, 'privacy/doc.html', context)

def keyword(request):
	kws = Keyword.objects.order_by('created_date')
	context = {'kws': kws}
	return render(request, 'privacy/keyword.html', context)

def about(request):
    return render(request, 'privacy/about.html')