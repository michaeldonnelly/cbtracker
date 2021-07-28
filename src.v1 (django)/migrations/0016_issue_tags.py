# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0015_auto_20170326_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(to='cbtracker.Tag'),
        ),
    ]
