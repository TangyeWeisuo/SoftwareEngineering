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
                    response = HttpResponseRedirect('/student/home/0')
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
            pe = int(request.POST['pe'])
            day = pe % 7
            period = pe / 7
            if models.Agenda.objects.filter(day=day, period=period, student=user):
                return HttpResponse("Existed.")
            else:
                agd = models.Agenda(
                    teacher=models.Teacher.objects.get(id=selected),
                    student=models.Student.objects.get(username=user),
                    day=day,
                    period=period,
                )
                agd.save()

        table = []
        for i in range(0, 5):
            table.append([])
        table[0].append('8:00-9:45')
        table[1].append('10:00-11:45')
        table[2].append('13:45-15:30')
        table[3].append('15:45-17:30')
        table[4].append('18:30-20:15')
        for i in range(0, 5):
            for j in range(0, 7):
                table[i].append([])
                table[i][j+1].append(0)
                table[i][j+1].append(i*7+j)

        super_student = models.Student.objects.get(id=9999)
        selection = models.Teacher.objects.get(id=selected)
        items = models.Agenda.objects.filter(teacher=selection)

        for item in items:
            if item.student == super_student:
                table[item.period][item.day+1][0] = 2
            else:
                table[item.period][item.day+1][0] = 1
        context = {
            'table': table,
                        }

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


def date(request):
    user = request.COOKIES.get('username')
    if user:
        if request.method == 'POST':
            the_teacher = request.POST.get('teacher')
            the_day = request.POST.get('day')
            the_period = request.POST.get('period')
            tc = models.Teacher.objects.get(username=the_teacher)
            usr = models.Student.objects.get(username=user)
            item = models.Agenda.objects.get(teacher=tc, student=usr, day=the_day, period=the_period)
            item.delete()
        stu = models.Student.objects.get(username=user)
        dt = models.Agenda.objects.filter(student=stu)
        context = {'list': dt}
        return render_to_response('Student/date.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login/')


def msg(request):
    pass
