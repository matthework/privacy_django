from django.shortcuts import render
from .models import Keyword


def main(request):
    kws = Keyword.objects.order_by('created_date')	
    return render(request, 'privacy/main.html', {'kws': kws})

def web(request):
	kws = Keyword.objects.order_by('created_date')
	return render(request, 'privacy/web.html', {'kws': kws})

def doc(request):
	kws = Keyword.objects.order_by('created_date')
	return render(request, 'privacy/doc.html', {'kws': kws})

def keyword(request):
	kws = Keyword.objects.order_by('created_date')
	return render(request, 'privacy/keyword.html', {'kws': kws})

def about(request):
    return render(request, 'privacy/about.html')