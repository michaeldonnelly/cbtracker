# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0012_auto_20170105_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesgrouper',
            name='pullList',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='own',
            field=models.BooleanField(default=False),
        ),
    ]
