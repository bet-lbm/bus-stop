# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-04 17:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stop',
            name='orientation',
        ),
        migrations.AddField(
            model_name='stop',
            name='reference',
            field=models.CharField(default=datetime.datetime(2017, 12, 4, 17, 21, 38, 893794, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stop',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
