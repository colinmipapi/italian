# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170313_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='dessing_quantity',
            new_name='dressing_quantity',
        ),
    ]
