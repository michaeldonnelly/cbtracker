# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0018_auto_20150711_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesGrouper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['name', 'start_year'], 'verbose_name_plural': 'series'},
        ),
        migrations.AddField(
            model_name='series',
            name='seriesGrouper',
            field=models.ForeignKey(to='comicbooks.SeriesGrouper', blank=True, null=True),
        ),
    ]
