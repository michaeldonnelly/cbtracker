# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0003_auto_20150710_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('issue_number', models.IntegerField()),
                ('own', models.BooleanField(default='true')),
                ('release_month', models.IntegerField()),
                ('release_year', models.IntegerField()),
                ('series', models.ForeignKey(to='comicbooks.Series')),
            ],
        ),
    ]
