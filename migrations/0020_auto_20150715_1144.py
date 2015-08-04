# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0019_auto_20150713_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-release_year', '-release_month', '-release_day', '-issue_number']},
        ),
        migrations.AlterModelOptions(
            name='seriesgrouper',
            options={'ordering': ['name']},
        ),
    ]
