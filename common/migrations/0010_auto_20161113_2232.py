# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20161112_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headpicture',
            name='priority',
            field=models.IntegerField(serialize=False, primary_key=True, unique=True),
        ),
    ]
