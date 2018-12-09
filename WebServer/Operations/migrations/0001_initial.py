# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('signer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('singer_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserFaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '咨询'), (4, '售后'), (5, '求购')], default=1)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.UserProfile')),
            ],
        ),
    ]