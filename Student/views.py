# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import *
from django.http import *
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
    try:
        user = request.COOKIES.get('username', '')
    except:
        return HttpResponseRedirect('/student/login/')
    messages = models.OpenMessage.objects.all()
    context = {'messages': messages}
    return render(request, 'Student/student_homepage.html', context)


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
                    print 'hh'
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


def agenda(request):
    user = request.COOKIES.get('username', '')
    if user:
        pass
    else:
        return HttpResponseRedirect('/login/')
