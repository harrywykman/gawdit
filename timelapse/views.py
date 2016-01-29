from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from timelapse.models import TimelapseProject, TimelapseImage, TimelapseVideo
from timelapse.tasks import (capture_image, capture_timelapse,
        create_timelapse_video, push_to_vimeo, timelapse)

@login_required
def timelapse_index(request):
    return render(request, "timelapse_index.html",
            {'projects': TimelapseProject.objects.all()})

@login_required
def timelapse_detail(request, pk):
    #project = TimelapseProject.objects.filter(pk=pk)[0]
    project = get_object_or_404(TimelapseProject, pk=pk)
    print "project: %s" % (project.name)
    return render(request, "timelapse_deets.html",
            {'project': project,})

@login_required
def capture_img(request, pk):
    project = get_object_or_404(TimelapseProject, pk=pk)
    capture_image.delay(project, project.number_frames)
    messages.success(request, """ Ran capture Image.""" )
    return HttpResponseRedirect(reverse('timelapse:timelapse_detail', args=(project.pk,)))

@login_required
def start_timelapse(request, pk):
    project = get_object_or_404(TimelapseProject, pk=pk)
    timelapse.delay(project)
    messages.success(request, """ Timelapse started. """ )
    return HttpResponseRedirect(reverse('timelapse:timelapse_detail', args=(project.pk,)))
