# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0020_auto_20150715_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 47, 36, 424604, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
