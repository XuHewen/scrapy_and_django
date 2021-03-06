# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20171117_0245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseresource',
            options={'verbose_name': '课程资源', 'verbose_name_plural': '课程资源'},
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='课程难度'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='学习时长'),
        ),
    ]
