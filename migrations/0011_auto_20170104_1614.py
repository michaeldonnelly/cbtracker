# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0010_auto_20170104_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='want',
            field=models.BooleanField(default=True),
        ),
    ]
