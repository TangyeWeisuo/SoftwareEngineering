from django.shortcuts import render
from django import forms
from system.models import Teacher,Lab
from django.shortcuts import render_to_response
# Create your views here.
'''def recommend(request):
    teacher_lst = Teacher.objects.all()
    teacher = []
    lab = []
    for t in teacher_lst:
        if not t.lab.Name in lab:
            print t.lab.Name
            teacher.append(t.Name)
            lab.append(t.lab.Name)
        else:
            pass
    return render_to_response('recommend.html',{'teachers': teacher})'''
def recommend(request):
    teacher_lst = Teacher.objects.all()
    teacher = []
    lab = []
    for t in teacher_lst:
        if not t.lab.Name in lab:
            teacher.append(t.Name)
            lab.append(t.lab.Name)
        else:
            pass
    if 'choice' in request.GET and request.GET['choice']:
        print request.GET['choice']
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        t = Teacher.objects.get(Name = name)
        print t.Name
        print t.Age
        return render_to_response('teacher_information.html',
                       {'teacher': t})
    else:
        return render_to_response('recommend.html',{'teachers': teacher})
        
def teacher_imformation(request):
    if 'name' in request.GET:
        teacher=Teacher.objects.get(Name = request.GET['name'])
    return render_to_response('teacher_information.html',{'teacher': teacher})