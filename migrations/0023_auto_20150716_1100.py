# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0022_series_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
