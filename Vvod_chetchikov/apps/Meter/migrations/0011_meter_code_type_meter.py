# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-01 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meter', '0010_remove_meter_code_type_meter'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='code_type_meter',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код счетчика'),
        ),
    ]
