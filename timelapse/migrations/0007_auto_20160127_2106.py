# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0006_auto_20160125_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelapseproject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
