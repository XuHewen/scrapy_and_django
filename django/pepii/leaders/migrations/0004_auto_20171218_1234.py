# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0003_auto_20171218_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderprofile',
            name='ethnicity',
            field=models.CharField(blank=True, default='汉族', max_length=10, null=True, verbose_name='民族'),
        ),
    ]