# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0007_auto_20160127_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelapseproject',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
