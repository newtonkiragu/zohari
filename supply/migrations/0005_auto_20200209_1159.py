# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-09 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_auto_20200209_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]