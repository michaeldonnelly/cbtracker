# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0016_issue_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(to='cbtracker.Tag'),
        ),
    ]
