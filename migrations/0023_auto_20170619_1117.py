# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtracker', '0022_issue_pulled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='pulled',
            new_name='pullList',
        ),
    ]
