# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discount_module', '0003_auto_20160408_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='negotiator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discount_module.Negotiator'),
            preserve_default=False,
        ),
    ]