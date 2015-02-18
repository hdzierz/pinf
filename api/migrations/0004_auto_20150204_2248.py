# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_fishscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fishscore',
            name='value',
        ),
        migrations.AddField(
            model_name='fishscore',
            name='values',
            field=jsonfield.fields.JSONField(default=dict, max_length=100),
            preserve_default=True,
        ),
    ]
