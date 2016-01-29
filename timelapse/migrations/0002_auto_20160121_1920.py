# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelapseImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name=b'date image created')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'timelapse_images')),
            ],
        ),
        migrations.AddField(
            model_name='timelapsevideo',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date timelapse created'),
        ),
    ]
