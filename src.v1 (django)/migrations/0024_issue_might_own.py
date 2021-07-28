# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0023_auto_20170619_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='might_own',
            field=models.BooleanField(default=False),
        ),
    ]
