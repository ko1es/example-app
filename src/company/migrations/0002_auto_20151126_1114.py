# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-26 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='lat',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='building',
            name='lon',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Longitude'),
        ),
    ]
