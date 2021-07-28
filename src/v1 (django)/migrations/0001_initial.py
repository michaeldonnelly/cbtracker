# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_number', models.IntegerField()),
                ('own', models.BooleanField(default='true')),
                ('release_day', models.IntegerField(default=0)),
                ('release_month', models.IntegerField()),
                ('release_year', models.IntegerField()),
                ('variant', models.CharField(max_length=100, blank=True)),
                ('story_name', models.CharField(max_length=100, blank=True)),
                ('story_part', models.IntegerField(blank=True, null=True)),
                ('fair_price', models.DecimalField(max_digits=5, blank=True, decimal_places=2, null=True)),
                ('price_source', models.CharField(max_length=100, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey('cbtracker.Author', models.SET_NULL, blank=True, null=True)),
            ],
            options={
                'ordering': ['-release_year', '-release_month', '-release_day', '-issue_number'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('issues', models.ManyToManyField(to='cbtracker.Issue', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('imprint_of', models.ForeignKey('cbtracker.Publisher', models.SET_NULL, blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_name', models.CharField(max_length=200, default='zzz')),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('start_year', models.IntegerField()),
                ('current', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey('cbtracker.Author', models.SET_NULL, blank=True, null=True)),
                ('publisher', models.ForeignKey('cbtracker.Publisher', models.SET_NULL, blank=True, null=True)),
            ],
            options={
                'ordering': ['name', 'start_year'],
                'verbose_name_plural': 'series',
            },
        ),
        migrations.CreateModel(
            name='SeriesGrouper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='series',
            name='seriesGrouper',
            field=models.ForeignKey('cbtracker.SeriesGrouper', models.SET_NULL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='series',
            field=models.ManyToManyField('cbtracker.Series', models.SET_NULL, blank=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='publisher',
            field=models.ForeignKey('cbtracker.Publisher', models.SET_NULL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='series',
            field=models.ForeignKey('cbtracker.Series', models.SET_NULL),
        ),
    ]
