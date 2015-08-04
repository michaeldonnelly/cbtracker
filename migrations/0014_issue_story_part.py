# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicbooks', '0013_issue_story_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='story_part',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
