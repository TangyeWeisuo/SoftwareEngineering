# -*-coding:utf-8-*-
from django.db import models


# Create your models here.
# class User(models.Model):
#     '''
#     The model of account.
#     '''
#     username = models.CharField(max_length=10)          # 用户名
#     password = models.CharField(max_length=15)          # 密码
#     email = models.EmailField(max_length=20)            # 邮箱


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
    writer = models.ForeignKey()                        # 消息发出者
    receiver = models.ForeignKey()                      # 消息接收者