# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-01 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_meter', '0005_auto_20171029_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_meter',
            name='type_meter',
        ),
    ]
