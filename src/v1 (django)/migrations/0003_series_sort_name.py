# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0002_remove_series_sort_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='sort_name',
            field=models.CharField(max_length=200, default='zzz'),
        ),
    ]
