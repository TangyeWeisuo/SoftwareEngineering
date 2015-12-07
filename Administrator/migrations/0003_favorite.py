# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20151127_2339'),
        ('Administrator', '0002_agenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(related_name='fs', to='Student.Student')),
                ('teacher', models.ForeignKey(related_name='ft', to='Student.Student')),
            ],
        ),
    ]
