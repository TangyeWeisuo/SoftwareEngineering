# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0003_remove_teacher_photo'),
        ('Student', '0003_remove_student_gpa'),
        ('Administrator', '0004_auto_20151128_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('teacher', models.ForeignKey(to='Teacher.Teacher')),
                ('writer', models.ForeignKey(to='Student.Student')),
            ],
        ),
    ]
