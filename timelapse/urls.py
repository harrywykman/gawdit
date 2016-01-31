from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.timelapse_index, name='timelapse_index'),
    url(r'^(?P<pk>[0-9]+)/$', views.timelapse_detail, name='timelapse_detail'),
    url(r'^(?P<pk>[0-9]+)/image_capture/$', views.capture_img, name='image_capture'),
    url(r'^(?P<pk>[0-9]+)/timelapse_capture/$', views.capture_timelapse, name='capture_timelapse'),
    url(r'^(?P<pk>[0-9]+)/timelapse_create/$', views.create_timelapse, name='create_timelapse'),
    url(r'^(?P<pk>[0-9]+)/timelapse_push/$', views.push_timelapse, name='push_timelapse'),
    url(r'^(?P<pk>[0-9]+)/timelapse_capture_push/$', views.capture_push_timelapse, name='capture_push_timelapse'),]
