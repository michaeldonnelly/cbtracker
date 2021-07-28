# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0027_auto_20170619_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='url_id_parameter',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='url_id_value',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='url_type_name',
        ),
    ]
