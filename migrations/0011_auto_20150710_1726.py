# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0010_auto_20150710_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='volume',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
