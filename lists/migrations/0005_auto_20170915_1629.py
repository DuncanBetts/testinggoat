# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_list_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]