# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='teacher',
            field=models.ForeignKey(related_name='ft', to='Teacher.Teacher'),
        ),
    ]
