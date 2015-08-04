# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0006_auto_20150710_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='publisher',
            field=models.ForeignKey(null=True, blank=True, to='comicbooks.Publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='imprint_of',
            field=models.ForeignKey(null=True, blank=True, to='comicbooks.Publisher'),
        ),
    ]
