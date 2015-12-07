# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import *
from django.http import *
from w3lib import url

from . import *
from django.template import RequestContext
from Administrator import models
from django import forms
# Create your views here.


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    email = forms.CharField(label='Email', max_length=30)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    check = forms.CharField(label='确认密码', widget=forms.PasswordInput())


def home(request, index):
    user = request.COOKIES.get('username')
    if user:
        messages = models.OpenMessage.objects.all()
        context = {'messages': messages}
        return render(request, 'Student/student_homepage.html', context)
    else:
        return HttpResponseRedirect('/student/login/')


def register(request):
    if request.POST:
        rf = RegisterForm(request.POST)
        if 'register' in request.POST:
            if rf.is_valid():
                username = rf.cleaned_data['username']
                email = rf.cleaned_data['email']
                password = rf.cleaned_data['password']
                check = rf.cleaned_data['check']
                if password == check:
                    student = models.Student(
                        username=username,
                        password=password,
                        email=email
                    )
                    student.save()
                    return HttpResponseRedirect('/student/login/')
                else:
                    return HttpResponseRedirect('/student/register/')
    else:
        rf = RegisterForm()
    return render_to_response('Student/register.html', {'rf': rf}, context_instance=RequestContext(request))


def login(request):
    if request.POST:
        lf = LoginForm(request.POST)
        if 'register' in request.POST:
            response = HttpResponseRedirect('/student/register/')
            return response
        else:
            if lf.is_valid():
                username = lf.cleaned_data['username']
                password = lf.cleaned_data['password']

                user = models.Student.objects.filter(username=username, password=password)
                if user:
                    response = HttpResponseRedirect('/student/home/0/')
                    response.set_cookie('username', username, 3600)
                    return response
                else:
                    return HttpResponseRedirect('/student/login/')
    else:
        lf = LoginForm()
    return render_to_response('Student/login.html', {'lf': lf}, context_instance=RequestContext(request))


# 定义4种状态,不可预约(2),已被预约(1),空闲(0)
# 当预约的时候,检查该时间段内该学生是否已有其他预约
def agenda(request, selected):
    user = request.COOKIES.get('username')
    if user:
        if request.method == 'POST':
            day = request.POST['day']
            period = request.POST['period']
            if models.Agenda.objects.filter(day=day, period=period, teacher=selected):
                return HttpResponse("Existed.")
            else:
                agd = models.Agenda(
                    teacher=models.Teacher.objects.get(id=selected),
                    student=models.Student.objects.get(username=user),
                    day=day,
                    period=period,
                )
                agd.save()
        bulldog0 = [0, 0, 0, 0, 0, 0, 0]
        bulldog1 = [0, 0, 0, 0, 0, 0, 0]
        bulldog2 = [0, 0, 0, 0, 0, 0, 0]
        bulldog3 = [0, 0, 0, 0, 0, 0, 0]
        bulldog4 = [0, 0, 0, 0, 0, 0, 0]
        table = []
        table.append(bulldog0)
        table.append(bulldog1)
        table.append(bulldog2)
        table.append(bulldog3)
        table.append(bulldog4)
        super_student = models.Student.objects.get(id=9999)
        selection = models.Teacher.objects.get(id=selected)
        items = models.Agenda.objects.filter(teacher=selection)
        for item in items:
            if item.student == super_student:
                table[item.period][item.day] = 2
            else:
                table[item.period][item.day] = 1
        for item in table[2]:
            print item
        print '--'
        for item in table[3]:
            print item
        context = {
            'time1': table[0],
            'time2': table[1],
            'time3': table[2],
            'time4': table[3],
            'time5': table[4]}

        return render_to_response('Student/agenda.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/student/login/')


def teacher(request, selected):
    pass


def favorite(request):
    user = request.COOKIES.get('username')
    if user:
        stu = models.Student.objects.get(username=user)
        favors = models.Favorite.objects.filter(student=stu)
        teachers = list({})
        for favor in favors:
            teachers.append(favor.teacher)
            print favor.teacher.age
        context = {'teachers': teachers}
        return render_to_response('Student/favorite.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login/')
