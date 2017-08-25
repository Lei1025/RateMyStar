# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 19:04
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20170820_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='AVG',
            field=models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2),
        ),
    ]
