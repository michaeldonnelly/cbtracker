# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0005_auto_20150821_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('volume', models.IntegerField()),
                ('own', models.BooleanField(default='true')),
                ('series', models.ForeignKey('cbtracker.Series', models.SET_NULL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-cover_year', '-cover_month', '-issue_number']},
        ),
    ]
