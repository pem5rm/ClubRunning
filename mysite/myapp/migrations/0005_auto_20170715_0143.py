# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170713_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='racetime',
            name='bib',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='racetime',
            name='score',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
