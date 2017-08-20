# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-20 17:35
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('Musicians', 'Musicians'), ('Authors', 'Authors'), ('Actors', 'Actors'), ('Athletes', 'Athletes'), ('Hosts', 'Hosts')], max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(default='Please uplaod a thumbnail picture.', upload_to='article/thumbnail')),
                ('banner', models.ImageField(default='Please upload a banner picture.', upload_to='article/banner')),
                ('content', models.TextField(max_length=10000)),
                ('author', models.ForeignKey(default='Username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('text', models.TextField(max_length=500)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.Article')),
            ],
        ),
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='rating/media/upload')),
            ],
        ),
        migrations.CreateModel(
            name='R_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='profile/user.png', upload_to='profile')),
                ('user', models.OneToOneField(default='new user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C1', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2)),
                ('C2', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2)),
                ('C3', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2)),
                ('C4', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2)),
                ('C5', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=2)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.Article')),
                ('user', models.ForeignKey(default='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.R_User'),
        ),
    ]
