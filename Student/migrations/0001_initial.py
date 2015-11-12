# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('age', models.PositiveIntegerField(verbose_name=0)),
                ('gender', models.BooleanField()),
                ('introduction', models.TextField()),
                ('major', models.CharField(max_length=10)),
                ('grade', models.PositiveIntegerField()),
                ('GPA', models.FloatField(verbose_name=0)),
            ],
        ),
    ]
