# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0018_auto_20170326_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(null=True, blank=True, to='cbtracker.Tag'),
        ),
        migrations.AlterField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(null=True, blank=True, to='cbtracker.Tag'),
        ),
    ]
