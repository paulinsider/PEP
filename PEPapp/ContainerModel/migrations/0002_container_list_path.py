# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContainerModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container_list',
            name='path',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
