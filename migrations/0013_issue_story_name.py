# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0012_auto_20150710_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='story_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
