# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RaceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(default=0)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('session', models.CharField(max_length=200)),
                ('event', models.CharField(max_length=200)),
            ],
        ),
    ]
