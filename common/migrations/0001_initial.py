# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=32)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('subject', models.CharField(blank=True, max_length=24, null=True)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
