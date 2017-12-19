# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0007_auto_20171218_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderprofile',
            options={'ordering': ('-id',), 'verbose_name': '\u9886\u5bfc\u4eba', 'verbose_name_plural': '\u9886\u5bfc\u4eba'},
        ),
        migrations.AlterField(
            model_name='leaderprofile',
            name='month_of_birth',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='\u51fa\u751f\u6708\u4efd'),
        ),
        migrations.AlterField(
            model_name='leaderprofile',
            name='year_of_birth',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u51fa\u751f\u5e74\u4efd'),
        ),
    ]