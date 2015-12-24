#-*- coding: UTF-8 -*-
# coding:utf-8

from django.shortcuts import render
from django import forms
from system.models import Teacher,Lab
from django.shortcuts import render_to_response
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def recommend(request):
    teacher_lst = Teacher.objects.all()
    teacher = []
    lab = []
    for t in teacher_lst:
        if not t.lab.name in lab:
            teacher.append(t.name)
            lab.append(t.lab.name)
        else:
            pass
    return render_to_response('search.html',{'teachers': teacher})
def choice_search(request):
    if 'choice' in request.GET and request.GET['choice']:
        cho = request.GET['choice']
        t = "老师"
        if cmp(cho,t) == 0:
            if 'name' in request.GET and request.GET['name']:
                name = request.GET['name']
                try:
                    t = Teacher.objects.get(name = name)
                    return render_to_response('information.html',
                               {'teacher': t})
                except:
                    return render_to_response('failed.html')
        else:
            if 'name' in request.GET and request.GET['name']:
                    name = request.GET['name']
                    try:
                        l = Lab.objects.get(name = name)
                        t = l.teacher_set.all()
                        return render_to_response('lab_teacher.html',
                                   {'teachers': t,'lab':l})
                    except:
                        return render_to_response('failed.html')

def teacher_imformation(request,name):
    try:
        teacher = Teacher.objects.get(name = name)
        return render_to_response('information.html',
                               {'teacher': teacher})
    except:
        pass