# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-19 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='autor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]