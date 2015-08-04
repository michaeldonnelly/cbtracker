# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0005_issue_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imprint_of', models.ForeignKey(null=True, to='comicbooks.Publisher')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='issue',
            name='publisher',
            field=models.ForeignKey(null=True, to='comicbooks.Publisher'),
        ),
    ]
