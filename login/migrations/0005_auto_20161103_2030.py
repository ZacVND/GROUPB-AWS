# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_merge_20161103_1737'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]