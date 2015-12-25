# -*-coding:utf-8-*-
from django.db import models
# from Teacher import *
# from Student import *
from Teacher.models import Teacher
from Teacher.models import Lab
from Student.models import Student


# Check the true information of each registering user before creating account.
# Fill the basic information of each student according to the true information.


class StudentList(models.Model):
    # The model of each student's true information.
    studentID = models.CharField(max_length=10)         # 学生学号
    name = models.CharField(max_length=10)              # 学生真实姓名
    grade = models.PositiveIntegerField()               # 学生年级
    gender = models.BooleanField()                      # 学生性别


class Message(models.Model):
    # The model of message, includes the content, writer and receiver.
    content = models.TextField()                        # 消息内容
    teacher = models.ForeignKey(Teacher)                # 教师
    student = models.ForeignKey(Student)                # 学生
    datetime = models.DateTimeField()                   # 日期时间


class OpenMessage(models.Model):
    # The model of message which are seen to all users.
    content = models.TextField()                        # 消息内容
    teacher = models.ForeignKey(Teacher)                # 消息发出者(教师)
    datetime = models.DateTimeField()                   # 日期时间


class Agenda(models.Model):
    # The model of agenda : {student} make an appointment with {teacher}
    # on {day}(0 for Monday, 1 for Tuesday and so on) at {period}(0 for 8:00 ~ 9:30 and so on)
    teacher = models.ForeignKey(Teacher)
    student = models.ForeignKey(Student)
    day = models.PositiveIntegerField()
    period = models.PositiveIntegerField()


class Favorite(models.Model):
    student = models.ForeignKey(Student, related_name='fs')
    teacher = models.ForeignKey(Teacher, related_name='ft')


class LeaveWord(models.Model):
    # The model of message which are seen to all users.
    content = models.TextField()                        #留言内容
    teacher = models.ForeignKey(Teacher)
    writer = models.ForeignKey(Student)                 #留言者
    datetime = models.DateTimeField(auto_now=True)                   # 日期时间
