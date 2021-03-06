# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 12:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格')),
                ('description', models.TextField(verbose_name='描述')),
                ('release_date', models.DateField(verbose_name='发布日期')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
