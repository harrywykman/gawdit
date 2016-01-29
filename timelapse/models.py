import datetime

from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

class TimelapseProject(models.Model):
    date_created = models.DateTimeField('date project created', default=timezone.now)
    name = models.CharField(max_length=100, unique=True)
    interval = models.IntegerField(default=5)
    number_frames = models.IntegerField(default=250)
    fps = models.IntegerField(default=25)
    #video_length = models.IntegerField("Length of timelapse video in minutes",default=1, null=True)

    def duration(self):
        seconds = self.number_frames / self.fps
        print "seconds: %s" % (seconds)
        m, s = divmod(seconds, 60)
        print "m: %s; s: %s" % (m, s)
        h, m = divmod(m, 60)
        print "h: %s; m: %s" % (h, m)
        return datetime.time(h, m, s).strftime("%H:%M:%S")

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

