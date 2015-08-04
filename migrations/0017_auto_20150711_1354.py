# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0016_issue_price_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-release_year', '-release_month']},
        ),
        migrations.AddField(
            model_name='issue',
            name='release_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
