# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-01 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_meter', '0006_remove_data_meter_type_meter'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_meter',
            name='type_meter',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Вид счетчика'),
        ),
    ]