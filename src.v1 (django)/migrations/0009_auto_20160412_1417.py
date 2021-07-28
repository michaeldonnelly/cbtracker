# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0008_auto_20160412_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ['series', 'volume']},
        ),
        migrations.AddField(
            model_name='trade',
            name='binding',
            field=models.IntegerField(choices=[(0, 'Paperback'), (1, 'Hardcover')], default=0),
        ),
    ]
