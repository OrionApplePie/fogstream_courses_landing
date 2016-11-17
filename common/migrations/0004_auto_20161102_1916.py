# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_headpicture_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headpicture',
            name='image',
            field=models.ImageField(upload_to='head/'),
        ),
    ]
