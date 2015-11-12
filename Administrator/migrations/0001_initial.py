# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('student', models.ForeignKey(to='Student.Student')),
                ('teacher', models.ForeignKey(to='Teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='OpenMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('teacher', models.ForeignKey(to='Teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentID', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('grade', models.PositiveIntegerField()),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
