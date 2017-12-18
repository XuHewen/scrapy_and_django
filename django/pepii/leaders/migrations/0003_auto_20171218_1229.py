# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0002_auto_20171218_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderprofile',
            name='ethnicity',
            field=models.CharField(default='汉族', max_length=10, verbose_name='民族'),
        ),
        migrations.AddField(
            model_name='leaderprofile',
            name='photo_img',
            field=models.URLField(blank=True, null=True, verbose_name='图片链接'),
        ),
        migrations.AddField(
            model_name='leaderprofile',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='出生地'),
        ),
        migrations.AddField(
            model_name='leaderprofile',
            name='purposed_position',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='拟任职位'),
        ),
        migrations.AddField(
            model_name='leaderprofile',
            name='remark',
            field=models.TextField(default=None, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='leaderprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='male', max_length=7, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='leaderprofile',
            name='position',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='现任职位'),
        ),
    ]
