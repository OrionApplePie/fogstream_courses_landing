# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_headpicture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='headpicture',
            name='ping',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='headpicture',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
