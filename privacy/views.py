from django.shortcuts import render
from .models import Keyword
from .mycode import doWeb
import html

def main(request):
    kws = Keyword.objects.order_by('created_date')	
    context = {'kws': kws}
    return render(request, 'privacy/main.html', context)

def web(request):
	kws = Keyword.objects.order_by('created_date')
	url = ""
	out = ""
	if request.GET.get('gobtn'):
		url = request.GET.get('url')
		out = doWeb(kws, url)
	context = {'kws': kws, 'out': out}
	return render(request, 'privacy/web.html', context)

def doc(request):
	kws = Keyword.objects.order_by('created_date')
	context = {'kws': kws}
	return render(request, 'privacy/doc.html', context)

def keyword(request):
	kws = Keyword.objects.order_by('created_date')
	context = {'kws': kws}
	return render(request, 'privacy/keyword.html', context)

def about(request):
    return render(request, 'privacy/about.html')