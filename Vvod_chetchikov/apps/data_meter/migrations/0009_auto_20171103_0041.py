# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-02 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_meter', '0008_data_meter_dannie'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_meter',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data_meter',
            name='type_meter',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Meter.Meter', verbose_name='Вид счётчика'),
            preserve_default=False,
        ),
    ]