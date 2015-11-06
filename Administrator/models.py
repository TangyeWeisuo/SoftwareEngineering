# -*-coding:utf-8-*-
from django.db import models


# Create your models here.
class User(models.Model):
    '''
    The model of account.
    '''
    username = models.CharField(max_length=10)          # 用户名
    password = models.CharField(max_length=15)          # 密码
    email = models.EmailField(max_length=20)            # 邮箱