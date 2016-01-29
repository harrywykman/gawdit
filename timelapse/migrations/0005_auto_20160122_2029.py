# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0004_auto_20160121_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelapseimage',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date image created'),
        ),
    ]
