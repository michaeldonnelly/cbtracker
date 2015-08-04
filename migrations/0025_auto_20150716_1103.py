# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import comicbooks.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0024_auto_20150716_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(default=comicbooks.models.made),
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 16, 3, 25, 329528, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(default=comicbooks.models.made),
        ),
        migrations.AddField(
            model_name='issue',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 16, 3, 27, 641874, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publisher',
            name='created',
            field=models.DateTimeField(default=comicbooks.models.made),
        ),
        migrations.AddField(
            model_name='publisher',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 16, 3, 31, 174318, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
