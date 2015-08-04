# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0009_issue_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='author',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='volume',
            field=models.IntegerField(null=True),
        ),
    ]
