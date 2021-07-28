# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0017_series_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuetag',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='issuetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='seriestag',
            name='series',
        ),
        migrations.RemoveField(
            model_name='seriestag',
            name='tag',
        ),
        migrations.DeleteModel(
            name='IssueTag',
        ),
        migrations.DeleteModel(
            name='SeriesTag',
        ),
    ]
