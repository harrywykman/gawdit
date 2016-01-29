
import datetime

from subprocess import call

from django.utils import timezone

from models import (
                    TimelapseProject, TimelapseImage, TimelapseVideo
                    )



TIMELAPSE_NAME = "test"

IMAGE_PATH = "/home/gerrard/pictures/timelapse/"

def new_timelapse_project(name):
    """
    Create a new project
    """
    project = TimelapseProject(name)
    return project

def capture_image(project):
    """ 
    capture image from camera 
    """
    time = timezone.now 
    name = project.name
    call(["fswebcam", "-r", "1280x720", "--no-banner", "%s%s.jpg" % (name, time)])

if __name__ == "__main__":
    project = new_timelapse_project("test")
    capture_image(project)
