# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0007_auto_20150710_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='publisher',
        ),
        migrations.AddField(
            model_name='series',
            name='publisher',
            field=models.ForeignKey(to='comicbooks.Publisher', blank=True, null=True),
        ),
    ]
