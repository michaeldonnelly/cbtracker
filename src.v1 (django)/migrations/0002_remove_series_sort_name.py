# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='sort_name',
        ),
    ]
