# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20161103_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headpicture',
            name='id',
        ),
        migrations.AlterField(
            model_name='headpicture',
            name='priority',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]