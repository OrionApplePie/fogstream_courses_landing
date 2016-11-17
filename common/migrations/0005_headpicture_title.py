# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20161102_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='headpicture',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
