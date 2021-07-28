# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0011_auto_20170104_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pullList',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='pullList',
            field=models.BooleanField(default=False),
        ),
    ]
