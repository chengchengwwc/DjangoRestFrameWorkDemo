# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 10:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(choices=[('male', 'man'), ('female', 'woman')], max_length=6)),
                ('gender', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('mobile', models.CharField(choices=[('male', 'man'), ('female', 'woman')], max_length=6)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
