# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-13 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190511_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfers_list',
            old_name='players',
            new_name='names',
        ),
        migrations.AddField(
            model_name='transfers_list',
            name='last_names',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]