# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punishment', '0002_auto_20171220_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punishmentmodel',
            options={'ordering': ('-id',), 'verbose_name': '\u5904\u7f5a\u4fe1\u606f', 'verbose_name_plural': '\u5904\u7f5a\u4fe1\u606f'},
        ),
    ]
