# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemarker', '0007_auto_20171114_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='timeTaken',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=4),
        ),
    ]