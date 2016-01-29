# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0005_auto_20160122_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelapseproject',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date project created'),
        ),
        migrations.AddField(
            model_name='timelapseproject',
            name='interval',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='timelapseproject',
            name='number_frames',
            field=models.IntegerField(default=250),
        ),
        migrations.AlterField(
            model_name='timelapseimage',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datetime image created'),
        ),
        migrations.AlterField(
            model_name='timelapseproject',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='timelapsevideo',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datetime timelapse created'),
        ),
    ]
