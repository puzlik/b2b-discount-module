# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discount_module', '0002_auto_20160408_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='debet',
            new_name='v_export',
        ),
        migrations.RenameField(
            model_name='agreement',
            old_name='kredit',
            new_name='v_import',
        ),
        migrations.AddField(
            model_name='period',
            name='agreement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discount_module.Agreement'),
            preserve_default=False,
        ),
    ]