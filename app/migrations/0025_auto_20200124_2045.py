# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-24 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_merge_20180311_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='timeTaken',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6),
        ),
    ]
