# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0011_auto_20150710_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(blank=True, null=True, to='comicbooks.Author'),
        ),
        migrations.AlterField(
            model_name='series',
            name='author',
            field=models.ForeignKey(blank=True, null=True, to='comicbooks.Author'),
        ),
    ]
