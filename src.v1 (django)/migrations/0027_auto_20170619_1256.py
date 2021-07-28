# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0026_auto_20170619_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='favorite',
            name='relative_url',
            field=models.CharField(default='foo', max_length=40),
            preserve_default=False,
        ),
    ]
