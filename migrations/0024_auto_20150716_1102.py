# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import comicbooks.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0023_auto_20150716_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesgrouper',
            name='created',
            field=models.DateTimeField(default=comicbooks.models.made),
        ),
        migrations.AddField(
            model_name='seriesgrouper',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 16, 2, 44, 961553, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
