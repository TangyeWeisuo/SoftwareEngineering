from django.shortcuts import render, render_to_response
from django.http import *
from django.http import *
from . import *
from django.template import RequestContext
from Administrator import models
# Create your views here.


def student_homepage(request, index):
    # if request.method == 'POST':
    #
    # else:
    #     raise Http404
    try:
        messages = models.OpenMessage.objects.all()
        context = {'messages': messages}
        return render(request, 'Student/student_homepage.html', context)
    except:
        raise Http404


def registerIndex(request):
    return render_to_response('Student/register.html')


def loginIndex(request):
    return render_to_response('Student/login.html')


def register(request):
    if request.POST:
        # exist = models.Student.objects.get(username=request.POST['username'])
        # raise Http404('User already existed')
        if request.POST['password'] != request.POST['check']:
            raise Http404("You typed different password.")
        student = models.Student(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        student.gender = True
        student.age = 21
        student.save()
        return render_to_response('Student/success.html')
        # raise Http404('1')
    else:
        raise Http404('2')


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            student = models.Student.objects.get(username=username)
        except:
            raise Http404("Username not existed.")
        if password == student.password:
            return render_to_response('Student/success.html')
        else:
            return render_to_response('Student/failed.html')
    else:
        raise Http404
