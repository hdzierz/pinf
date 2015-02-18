# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishob',
            name='form_completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
