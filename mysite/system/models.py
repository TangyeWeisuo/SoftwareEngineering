from django.db import models

# Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=20)   
    introduction = models.TextField()       
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.BooleanField()
    subject = models.CharField(max_length = 10)
    lab = models.ForeignKey(Lab)   
    