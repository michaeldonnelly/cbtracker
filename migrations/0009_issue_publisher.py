# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0008_auto_20150710_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='publisher',
            field=models.ForeignKey(to='comicbooks.Publisher', null=True, blank=True),
        ),
    ]
