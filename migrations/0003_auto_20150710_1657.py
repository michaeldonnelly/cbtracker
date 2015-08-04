# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0002_auto_20150710_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
