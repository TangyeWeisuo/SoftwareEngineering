# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('introduction', models.TextField()),
                ('photo', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('age', models.PositiveIntegerField(verbose_name=0)),
                ('gender', models.BooleanField()),
                ('photo', models.FileField(upload_to=b'')),
                ('introduction', models.TextField()),
                ('agenda', models.CharField(max_length=7, verbose_name=b'0000000')),
                ('foundation', models.TextField()),
                ('subject', models.CharField(max_length=10)),
                ('lab', models.ForeignKey(to='Teacher.Lab')),
            ],
        ),
    ]
