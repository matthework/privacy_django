# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privacy', '0002_auto_20170114_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='author',
        ),
    ]
