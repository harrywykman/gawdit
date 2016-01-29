from django.conf.urls import patterns, url
from django.contrib.auth import authenticate, login

from . import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    #(r'^login/$', 'django.contrib.auth.views.login'),
)
