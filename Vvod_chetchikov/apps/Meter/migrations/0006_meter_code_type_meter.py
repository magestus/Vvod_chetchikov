# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-29 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meter', '0005_remove_meter_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='code_type_meter',
            field=models.CharField(max_length=10),
        ),
    ]
