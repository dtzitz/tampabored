# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_event_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_url',
            field=models.URLField(default='https://res.cloudinary.com/dtzitz/image/upload/v1467560008/AOjKtQy_jxytxw.jpg'),
        ),
    ]
