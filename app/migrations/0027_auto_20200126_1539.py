# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-26 15:39
from __future__ import unicode_literals

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_assessment_max_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=django_mysql.models.EnumField(choices=[('start', 'start'), ('in_progress', 'in_progress'), ('complete', 'complete'), ('overtime', 'overtime')]),
        ),
    ]
