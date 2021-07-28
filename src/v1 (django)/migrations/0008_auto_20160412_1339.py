# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0007_trade_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='release_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='release_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
