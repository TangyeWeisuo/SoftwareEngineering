# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20151127_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='GPA',
        ),
    ]
