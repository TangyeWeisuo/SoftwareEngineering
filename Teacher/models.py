# -*- coding: cp936 -*-
from django.db import models

# Create your models here.


class Lab(models.Model):
    # The model of laboratory.
    name = models.CharField(max_length=20)
    introduction = models.TextField()


class Teacher(models.Model):
    # The model of teacher.
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    email = models.EmailField(max_length=20,null=True)
    name = models.CharField(max_length=30,null=True)
    age = models.PositiveIntegerField(verbose_name=0, null=True)
    gender = models.BooleanField(default=1)
    photo = models.ImageField(upload_to='img', null=True)
    introduction = models.TextField(null=True)
    foundation = models.TextField(null=True)
    subject = models.CharField(max_length=10, null=True)
    lab = models.ForeignKey(Lab, null=True)



