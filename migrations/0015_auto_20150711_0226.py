# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0014_issue_story_part'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'series'},
        ),
        migrations.AddField(
            model_name='issue',
            name='fair_price',
            field=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2),
        ),
    ]
