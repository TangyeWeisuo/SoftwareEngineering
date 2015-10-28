# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class Lab(models.Model):
    name = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField(verbose_name=0)
    gender = models.BooleanField()
    photo = models.FileField()
