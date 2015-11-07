# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class Lab(models.Model):
    # The model of laboratory.
    name = models.CharField(max_length=20)  # 实验室名称
    introduction = models.TextField()       # 实验室简介
    photo = models.FilePathField()          # 实验室照片


class Teacher(models.Model):
    # The model of teacher.
    username = models.CharField(max_length=10)              # 用户名
    password = models.CharField(max_length=15)              # 密码
    email = models.EmailField(max_length=20)                # 邮箱
    name = models.CharField(max_length=10)                  # 教师姓名
    age = models.PositiveIntegerField(verbose_name=0)       # 教师年龄
    gender = models.BooleanField()                          # 教师性别
    photo = models.FileField()                              # 教师照片
    introduction = models.TextField()                       # 教师简介
    agenda = models.CharField(verbose_name='0000000')       # 教师日程
    foundation = models.TextField()                         # 教师基金
    subject = models.CharField(max_length=10)               # 教师教学科目
    lab = models.ForeignKey(Lab)                            # 教师所属实验室


