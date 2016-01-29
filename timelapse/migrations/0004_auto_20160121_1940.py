# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0003_auto_20160121_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timelapse',
            new_name='TimelapseProject',
        ),
    ]
