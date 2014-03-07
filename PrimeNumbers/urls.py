from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'primes.views.index'),
    url(r'^prime/', 'primes.views.get_prime'),
    url(r'^json/prime/(?P<index>\d+)', 'primes.views.get_prime_json'),
)
