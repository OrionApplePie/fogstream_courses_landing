# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_ourteam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headpicture',
            old_name='ping',
            new_name='interval',
        ),
    ]
