# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount_module', '0002_auto_20160410_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='v_export',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='v_import',
            field=models.IntegerField(blank=True),
        ),
    ]