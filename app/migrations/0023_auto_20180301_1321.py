# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20180301_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('created_at',), 'permissions': (('change_courses_users', 'Can change courses_users'),)},
        ),
    ]