# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-07-28 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='mileage',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='motor_potency',
            field=models.CharField(db_index=True, max_length=15),
        ),
    ]
