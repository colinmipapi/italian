# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170313_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_one',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/blog/media/uploads'),
        ),
    ]
