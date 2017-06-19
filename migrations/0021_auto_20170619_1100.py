# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0020_issue_reading_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='special',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cbtracker.Tag'),
        ),
        migrations.AlterField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cbtracker.Tag'),
        ),
    ]
