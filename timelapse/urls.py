from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.timelapse_index, name='timelapse_index'),
    url(r'^(?P<pk>[0-9]+)/$', views.timelapse_detail, name='timelapse_detail'),
    url(r'^(?P<pk>[0-9]+)/capture/$', views.capture_img, name='capture_img'),
    url(r'^(?P<pk>[0-9]+)/start/$', views.start_timelapse, name='start_timelapse'),]
