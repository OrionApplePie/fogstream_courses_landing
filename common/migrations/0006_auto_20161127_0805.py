# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20161127_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['timestamp'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
