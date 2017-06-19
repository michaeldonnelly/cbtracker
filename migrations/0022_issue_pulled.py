# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0021_auto_20170619_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='pulled',
            field=models.BooleanField(default=False),
        ),
    ]
