# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_auto_20151127_2339'),
        ('Student', '0002_auto_20151127_2339'),
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.PositiveIntegerField()),
                ('period', models.PositiveIntegerField()),
                ('student', models.ForeignKey(to='Student.Student')),
                ('teacher', models.ForeignKey(to='Teacher.Teacher')),
            ],
        ),
    ]
