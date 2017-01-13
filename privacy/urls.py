from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^web/$', views.web, name='web'),
    url(r'^doc/$', views.doc, name='doc'),
    url(r'^keyword/$', views.keyword, name='keyword'),
    url(r'^about/$', views.about, name='about'),
]