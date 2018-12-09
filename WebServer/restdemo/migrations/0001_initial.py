# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-01 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.TextField()),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('style', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
