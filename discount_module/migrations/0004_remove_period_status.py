# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount_module', '0003_auto_20160410_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='status',
        ),
    ]