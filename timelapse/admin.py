from django.contrib import admin

from embed_video.admin import AdminVideoMixin
from .models import TimelapseVideo, TimelapseImage, TimelapseProject

class TimelapseVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('name', 'video',)                                                 
    ordering = ('name',)

admin.site.register(TimelapseProject)
admin.site.register(TimelapseVideo, TimelapseVideoAdmin)
admin.site.register(TimelapseImage)

