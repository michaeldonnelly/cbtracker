# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0027_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='issues',
            field=models.ManyToManyField(to='comicbooks.Issue', blank=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='series',
            field=models.ManyToManyField(to='comicbooks.Series', blank=True),
        ),
    ]
