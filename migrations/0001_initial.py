# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.TextField()),
                ('author', models.TextField()),
                ('volume', models.IntegerField()),
                ('start_year', models.IntegerField()),
                ('current', models.BooleanField()),
            ],
        ),
    ]
