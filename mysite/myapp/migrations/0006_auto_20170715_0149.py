# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170715_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='racetime',
            name='host',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='racetime',
            name='location',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
