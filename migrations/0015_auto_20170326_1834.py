# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0014_issue_annual'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(to='cbtracker.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='SeriesTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('series', models.ForeignKey(to='cbtracker.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='seriestag',
            name='tag',
            field=models.ForeignKey(to='cbtracker.Tag'),
        ),
        migrations.AddField(
            model_name='issuetag',
            name='tag',
            field=models.ForeignKey(to='cbtracker.Tag'),
        ),
    ]
