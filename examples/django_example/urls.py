try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.shortcuts import render


def my_view(request):
    # View code here...
    return render(request, 'test.jade', {"foo": "bar"})

urlpatterns = patterns(
    '',
    url(r'^$', my_view, name='home'),
)
