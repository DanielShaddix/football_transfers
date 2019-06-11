# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-11 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190507_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfers_list',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfers_list',
            name='club',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfers_list',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transfers_list',
            name='players',
            field=models.CharField(max_length=50),
        ),
    ]