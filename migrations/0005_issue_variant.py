# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0004_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='variant',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
