from django.db import models

class Enter(models.Model):
    studentnumber  = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=15)



class Student(models.Model):
    # The model of student.
    username = models.CharField(max_length=10)              #
    password = models.CharField(max_length=15)              #
    email = models.EmailField(max_length=20)                #
    name = models.CharField(max_length=10)                  #
    age = models.PositiveIntegerField(verbose_name=0)       #
    gender = models.BooleanField()                          #
    introduction = models.TextField()                       #
    major = models.CharField(max_length=10)                 #
    grade = models.PositiveIntegerField()                   #
    GPA = models.FloatField(verbose_name=0)                 #