# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_saveurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yandex_metricks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yandex', models.CharField(max_length=155)),
            ],
        ),
    ]