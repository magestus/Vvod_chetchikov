# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-29 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meter', '0006_meter_code_type_meter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='code_type_meter',
            field=models.TextField(default='', max_length=10, verbose_name='Код счетчика'),
        ),
    ]
