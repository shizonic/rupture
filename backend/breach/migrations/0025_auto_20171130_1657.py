# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-30 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breach', '0024_auto_20170601_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampleset',
            name='data',
        ),
        migrations.AddField(
            model_name='sampleset',
            name='datalength',
            field=models.IntegerField(default=0, help_text='The length of the raw data collected on the network for this sampleset'),
        ),
    ]
