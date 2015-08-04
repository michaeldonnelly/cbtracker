# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0025_auto_20150716_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='seriesgrouper',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
