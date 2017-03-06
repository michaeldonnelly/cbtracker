# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0013_auto_20170105_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='annual',
            field=models.BooleanField(default=False),
        ),
    ]
