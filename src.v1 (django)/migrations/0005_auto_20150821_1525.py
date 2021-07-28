# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0004_auto_20150804_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='cover_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='cover_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='release_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='release_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
