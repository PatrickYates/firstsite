# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.TextField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]
