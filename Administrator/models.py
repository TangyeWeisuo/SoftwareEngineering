# -*-coding:utf-8-*-
from django.db import models
# from Teacher import *
# from Student import *
from Teacher.models import Teacher
from Student.models import Student


# Check the true information of each registering user before creating account.
# Fill the basic information of each student according to the true information.


class StudentList(models.Model):
    # The model of each student's true information.
    ID = models.CharField(max_length=10)                # 学生学号
    name = models.CharField(max_length=10)              # 学生真实姓名
    grade = models.PositiveIntegerField()               # 学生年级
    gender = models.BooleanField()                      # 学生性别


class Message(models.Model):
    # The model of message, includes the content, writer and receiver.
    content = models.TextField()                        # 消息内容
    teacher = models.ForeignKey(Teacher)                # 教师
    student = models.ForeignKey(Student)                # 学生


class OpenMessage(models.Model):
    # The model of message which are seen to all users.
    content = models.TextField()                        # 消息内容
    teacher = models.ForeignKey(Teacher)                # 消息发出者(教师)