# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-19 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]