import os, os.path
import time
import datetime
import vimeo
import requests

from subprocess import call
from moviepy.editor import *

from django.core.files import File
from django.utils import timezone

from timelapse.models import (
                    TimelapseProject, TimelapseImage, TimelapseVideo
                    )

#ACCESS_TOKEN = '35f21bf2ac2d194b3d3354fb67ced684'
ACCESS_TOKEN = '99de9beecdc80a53d56f2731a00cf7fb' # public private purchased create edit delete interact upload
CLIENT_ID = 'a0252bed7f0d5917db154ec54ad95e2a19fdd8c0'
CLIENT_SECRET = 'awXefnxEBjMZ67nW61JpNv0h2MZis4/m2X4ld8sNCJAWcyf1o1rvG+FXIrNiigtRdXBygeXPVDeON+n14BkAxG5d4IeRsrRUvc2FQT4HdSbQzGCxP5+DXKuOd1dTVmO2'
PROJECT = "sleeping"
FRAMES = 25
FILETYPE = "jpg"
INTERVAL = 20 
NUMBER_FRAMES = 1440


def new_timelapse_project(name, internal, number_frames):
    """
    Create a new project
    """
    tp = TimelapseProject.objects.filter(name=name)[0]
    if tp:
        return tp
    else:
        project = TimelapseProject(name=name)
        project.save()
        print project
        return project

def capture_image(project, number):
    """
    capture image from camera
    """
    #now = datetime.datetime.now()
    #now_str = now.strftime('%Y%m%d:%H:%M:%S')
    #print now_str
    name = project.name
    #print name
    image_number = str(number).zfill(7)
    call(["mkdir", "./timelapse_images/%s/" % (name)])
    path = "./timelapse_images/%s/" % (name)
    filename = "%s_%s.jpg" % (name, image_number)
    call(["fswebcam", "-r", "1280x720", "--no-banner", "%s%s" % (path, filename)])
    image = File(open('%s%s' % (path, filename), 'r'))
    ti = TimelapseImage(name=name, image=image, timelapse=project)
    ti.save()
    print "photo taken"

def capture_timelapse(project):
    for n in range(project.number_frames):
        capture_image(project, n)
        time.sleep(project.interval)

def create_timelapse_video(project):
    frames = FRAMES
    filetype = FILETYPE
    name = project.name
    img_path = "./timelapse_images/%s/" % (name)
    video_path = "./timelapse_video/%s/" % (name)
    call(["mkdir", "./timelapse_video/%s/" % (name)])
    call(["ffmpeg", "-y", "-pattern_type", "glob", "-i",
          "%s*.%s" % (img_path, filetype), "-vcodec",
          "libx264", "%s%s.mp4" % (video_path, name)])
    print "video complete"
#    images = project.timelapseimage_set.all().order_by('date_created')
    #names = [img_path + name for name in os.listdir(img_path) if name[-4:] == ".jpg"]
#    print images
#    names = []
#    for image in images:
#        names.append(image.image.name)
#    print names
    #clip = ImageSequenceClip(names, fps=frames)
#    clip = ImageSequenceClip(img_path, fps=frames)
#    os.mkdir(video_path)
#    clip.write_videofile('%s%s.mp4' % (video_path, name), fps=frames, codec='mpeg4')

def add_project_to_images(project):
    images = TimelapseImage.objects.filter(name=project.name)
    print images
    for image in images:
        image.timelapse = project
        image.save()
        print image


def push_to_vimeo(project):
    v = vimeo.VimeoClient(token=ACCESS_TOKEN, key=CLIENT_ID, secret=CLIENT_SECRET)
    filename = "./timelapse_video/%s/%s.mp4" % (project.name, project.name)
    uri = v.upload(filename)
    ref = uri.split('/')[2]
    url = "http://vimeo.com/%s/" % (ref)
    video = TimelapseVideo(timelapse=project, name=project.name, video=url)
    video.save()
    print set_remote_video_title(ACCESS_TOKEN, uri, project.name)

def set_remote_video_title(access_token, video_uri, title):                                                         
    payload = {'name': title}                                                                                       
    video_full_url = "https://api.vimeo.com%s" % (video_uri)                                                        
    print "Set video title. Url is %s and payload is %s" % (video_full_url, payload)                                
    #print "Setting access_token %s in the Authorization header" % access_token                                     
    auth_headers = {'Authorization': 'Bearer ' + access_token}                                                      
    print auth_headers                                                                                              
    return requests.patch("https://api.vimeo.com%s" % (video_uri), data=payload, headers=auth_headers)


#def set_remote_video_title(access_token, video_uri, title, description, privacy):
#    payload = {'name': title, 'description': description, 'privacy.view': privacy}
#    video_full_url = "api.vimeo.com"; + video_uri
#    print "Set video title. Url is %s and payload is %s" % (video_full_url, payload)
#    #print "Setting access_token %s in the Authorization header" % access_token
#    auth_headers = {'Authorization': 'Bearer ' + access_token}
#    print auth_headers
#    return requests.patch("api.vimeo.com" + video_uri, data=payload, headers=auth_headers)

project = TimelapseProject(name=PROJECT, interval=INTERVAL, number_frames=NUMBER_FRAMES)
project.save()
#project = TimelapseProject.objects.filter(name="testing")[0]
#add_project_to_images(project)
#capture_image(project)
capture_timelapse(project)
create_timelapse_video(project)
push_to_vimeo(project)
