# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0015_auto_20150711_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='price_source',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
