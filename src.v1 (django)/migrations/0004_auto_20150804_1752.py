# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0003_series_sort_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['sort_name', 'start_year'], 'verbose_name_plural': 'series'},
        ),
        migrations.AlterField(
            model_name='series',
            name='sort_name',
            field=models.CharField(max_length=200),
        ),
    ]
