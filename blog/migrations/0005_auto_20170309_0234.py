# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170309_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
