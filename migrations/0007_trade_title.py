# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0006_auto_20160412_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
