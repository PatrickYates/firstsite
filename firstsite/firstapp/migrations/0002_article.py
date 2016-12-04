# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
