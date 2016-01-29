# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapse', '0002_auto_20160121_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timelapse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='timelapseimage',
            name='timelapse',
            field=models.ForeignKey(to='timelapse.Timelapse', null=True),
        ),
        migrations.AddField(
            model_name='timelapsevideo',
            name='timelapse',
            field=models.ForeignKey(to='timelapse.Timelapse', null=True),
        ),
    ]
