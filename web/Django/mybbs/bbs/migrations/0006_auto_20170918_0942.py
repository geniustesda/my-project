# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20170918_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(blank=True, null=True, verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
