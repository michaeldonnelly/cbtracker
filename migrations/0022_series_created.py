# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import comicbooks.models


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0021_series_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='created',
            field=models.DateTimeField(default=comicbooks.models.made),
        ),
    ]
