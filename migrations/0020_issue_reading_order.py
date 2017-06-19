# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0019_auto_20170326_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='reading_order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
