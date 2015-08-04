# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0017_auto_20150711_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-release_year', '-release_month', '-release_day']},
        ),
        migrations.AlterField(
            model_name='issue',
            name='release_day',
            field=models.IntegerField(default=0),
        ),
    ]
