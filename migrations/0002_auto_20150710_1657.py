# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]
