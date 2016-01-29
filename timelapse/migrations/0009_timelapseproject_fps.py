# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0008_auto_20160127_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelapseproject',
            name='fps',
            field=models.IntegerField(default=25),
        ),
    ]
