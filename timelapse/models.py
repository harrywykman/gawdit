import datetime
import os

from django.db import models
from django.utils import timezone
from django.conf import settings

from embed_video.fields import EmbedVideoField

VIDEO_PATH = "%s/timelapse_video/" % (settings.MEDIA_ROOT)

class Camera(models.Model):

    class Meta:
        abstract = True

    def capture_image(filename, resolution, ):
        pass

class RPICamera(Camera):
    pass

class WebCamera(Camera):
    pass



class TimelapseProject(models.Model):
    date_created = models.DateTimeField('date project created', default=timezone.now)
    name = models.CharField(max_length=100, unique=True)
    interval = models.IntegerField(default=5)
    number_frames = models.IntegerField(default=250)
    fps = models.IntegerField(default=25)
    #video_length = models.IntegerField("Length of timelapse video in minutes",default=1, null=True)

    def video_file_exists(self):
        # TODO should not be hardcoded
        #base = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
        path = "%s/%s/%s.mp4" % (VIDEO_PATH, self.name, self.name)
#        return os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
 #       return os.path.split(path)[0]
        return os.path.exists(path)

    def seconds_to_hms(self, seconds):
        print "seconds: %s" % (seconds)
        m, s = divmod(seconds, 60)
        print "m: %s; s: %s" % (m, s)
        h, m = divmod(m, 60)
        print "h: %s; m: %s" % (h, m)
        return datetime.time(h, m, s).strftime("%H:%M:%S")

    def timelapse_runtime(self):
        seconds = self.interval * self.number_frames
        return self.seconds_to_hms(seconds)

    def duration_video(self):
        seconds = self.number_frames / self.fps
        return self.seconds_to_hms(seconds)

    def latest_image(self):
        return self.timelapseimage_set.latest("date_created")

    def video(self):
        return self.timelapsevideo_set.all()

    def __unicode__(self):
        return "Timelapse Project: %s" % (self.name)

class TimelapseVideo(models.Model):
    timelapse = models.ForeignKey(TimelapseProject, null=True)
    date_created = models.DateTimeField('datetime timelapse created', default=timezone.now)
    name = models.CharField(max_length=100)
    video = EmbedVideoField()

    def start_date(self):
        return self.timelapse.timelapseimage_set.earliest("date_created").date_created

    def end_date(self):
        return self.timelapse.timelapseimage_set.latest("date_created").date_created

    def __unicode__(self):
        return "Timelapse Video: %s" % (self.name)


class TimelapseImage(models.Model):
    timelapse = models.ForeignKey(TimelapseProject, null=True)
    date_created = models.DateTimeField('datetime image created', default=timezone.now)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="timelapse_images")

    def __unicode__(self):
        return "Timelapse Image: %s --- %s" % (self.name, self.date_created)

