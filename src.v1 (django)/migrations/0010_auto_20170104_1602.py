# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0009_auto_20160412_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
