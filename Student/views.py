# -*- coding:utf-8 -*-
import sys
from django.shortcuts import render, render_to_response
from django.http import *
from django.http import *
from w3lib import url

from . import *
from django.template import RequestContext
from Administrator import models
from django import forms
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    email = forms.CharField(label='Email', max_length=30)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    check = forms.CharField(label='确认密码', widget=forms.PasswordInput())


def home(request, current):
    user = request.COOKIES.get('username')
    if user:
        NUM = 10
        index = []
        current = int(current)
        messages = models.OpenMessage.objects.all()
        total = len(messages)
        pages = total / NUM
        if total % NUM != 0:
            pages += 1

        i = -2
        while i <= 2:
            if 1 <= current + i <= pages:
                index.append(current + i)
            i += 1

        first = [1]
        last = [pages]

        begin = (current - 1) * NUM
        end = min(NUM * current - 1, total - 1)
        begin = total - begin
        end = total - end
        show = []
        for i in range(begin - 1, end - 2, -1):
            show.append(messages[i])

        context = {'messages': show,
                   'current': current,
                   'index': index,
                   'first': first,
                   'last': last,
                   }
        return render(request, 'Student/student_homepage.html', context)
    else:
        return HttpResponseRedirect('/student/login/')


def msg(request, current):
    user = request.COOKIES.get('username')
    if user:
        NUM = 10
        index = []
        current = int(current)
        stu = models.Student.objects.get(username=user)
        fav = models.Favorite.objects.filter(student=stu)
        ms = models.OpenMessage.objects.all()
        messages = []
        for item in ms:
            for favor in fav:
                if item.teacher == favor.teacher:
                    messages.append(item)

        total = len(messages)
        pages = total / NUM
        if total % NUM != 0:
            pages += 1

        i = -2
        while i <= 2:
            if 1 <= current + i <= pages:
                index.append(current + i)
            i += 1

        first = [1]
        last = [pages]

        begin = (current - 1) * NUM
        end = min(NUM * current - 1, total - 1)
        begin = total - begin
        end = total - end
        show = []
        for i in range(begin - 1, end - 2, -1):
            print i
            show.append(messages[i])

        context = {'messages': show,
                   'current': current,
                   'index': index,
                   'first': first,
                   'last': last,
                   }
        return render(request, 'Student/subscribe.html', context)
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
            return HttpResponseRedirect('/student/login/')
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
                    response = HttpResponseRedirect('/student/home/1')
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
            'selected': selected,
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
        if favors:
            teachers = []
            for favor in favors:
                teachers.append(favor.teacher)
                print favor.teacher.age
            context = {'teachers': teachers}
            return render_to_response('Student/favorite.html', context, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/student/search')
    else:
        return HttpResponseRedirect('/student/login/')


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
        return HttpResponseRedirect('/student/login/')


def recommend(request):
    user = request.COOKIES.get('username')
    if user:
        teacher_lst = models.Teacher.objects.all()
        teacher_ = []
        lab = []
        for t in teacher_lst:
            if not t.lab.name in lab:
                teacher_.append(t)
                lab.append(t.lab.name)
            else:
                pass

        if request.method == 'POST':
            usrname = request.POST.get('usrname')
            stu = models.Student.objects.get(username=user)
            tc = models.Teacher.objects.get(username=usrname)
            if not models.Favorite.objects.filter(student=stu, teacher=tc):
                fav = models.Favorite(
                    teacher=tc,
                    student=stu
                )
                fav.save()

        return render_to_response('Student/search.html', {'teachers': teacher_})
    else:
        return HttpResponseRedirect('/student/login/')


def choice_search(request):
    user = request.COOKIES.get('username')
    if user:
        if 'choice' in request.GET and request.GET['choice']:
            cho = request.GET['choice']
            t = "老师"
            if cmp(cho, t) == 0:
                if 'name' in request.GET and request.GET['name']:
                    name = request.GET['name']
                    try:
                        t = models.Teacher.objects.get(name=name)
                        return render_to_response('Student/information.html',
                                   {'teacher': t})
                    except:
                        return render_to_response('Student/failed.html')
            else:
                if 'name' in request.GET and request.GET['name']:
                        name = request.GET['name']
                        try:
                            l = models.Lab.objects.get(name=name)
                            t = l.teacher_set.all()
                            return render_to_response('Student/lab_teacher.html',
                                       {'teachers': t, 'lab': l})
                        except:
                            return render_to_response('Student/failed.html')

    else:
        return HttpResponseRedirect('/student/login/')


def teacher_information(request, selected):
    user = request.COOKIES.get('username')
    if user:
        teacher_ = models.Teacher.objects.get(pk=selected)
        if request.method == 'POST':
            usrname = request.POST.get('usrname')
            stu = models.Student.objects.get(username=user)
            tc = models.Teacher.objects.get(username=usrname)
            if not models.Favorite.objects.filter(student=stu, teacher=tc):
                fav = models.Favorite(
                    teacher=tc,
                    student=stu
                )
                fav.save()
        return render_to_response('Student/information.html',
                                    {'teacher': teacher_})
    else:
        return HttpResponseRedirect('/student/login')



def logout(request):
    user = request.COOKIES.get('username')
    if user:
        response = HttpResponseRedirect('/student/login')
        response.delete_cookie('username')
        return response
    else:
        return HttpResponseRedirect('/student/login')


def studentview(request):
    user = request.COOKIES.get('username')
    if user:
        student = models.Student.objects.get(username=user)
        if request.POST:
            student.password = request.POST.get('password')
            student.email = request.POST.get('email')
            student.name = request.POST.get('name')
            student.age = request.POST.get('age')
            student.introduction = request.POST.get('introduction')
            student.major = request.POST.get('major')
            student.grade = request.POST.get('grade')
            student.GPA = request.POST.get('GPA')
            if request.POST.get('gender') == 'M':
                student.gender = True
            else:
                student.gender = False

            student.save()
        return render_to_response('Student/studentview.html', {'student': student})
    else:
        return HttpResponseRedirect('/student/login/')


def tinfo(request, selected):
    user = request.COOKIES.get('username')
    if user:
        tc = models.Teacher.objects.get(id=selected)
        return render_to_response('Student/TeacherInformation.html', {'teacher': tc, 'selected': selected})
    else:
        return HttpResponseRedirect('/student/login/')


def tmessage(request, selected, current):
    user = request.COOKIES.get('username')
    if user:
        tc = models.Teacher.objects.get(id=selected)
        OpenMessages = models.OpenMessage.objects.filter(teacher=tc)

        NUM = 10
        index = []
        current = int(current)
        total = len(OpenMessages)
        pages = total / NUM
        if total % NUM != 0:
            pages += 1

        i = -2
        while i <= 2:
            if 1 <= current + i <= pages:
                index.append(current + i)
            i += 1

        first = [1]
        last = [pages]

        begin = (current - 1) * NUM
        end = min(NUM * current - 1, total - 1)
        begin = total - begin
        end = total - end
        show = []
        for i in range(begin - 1, end - 2, -1):
            show.append(OpenMessages[i])

        return render_to_response('Student/TeacherHomepage.html', {'current': current,
                                                          'index': index,
                                                          'teacher': teacher,
                                                          'first': first,
                                                          'last': last,
                                                          'openmessages': show,
                                                          'selected': selected,})
    else:
        return HttpResponseRedirect("/student/login/")


def tboard(request, selected, current):
    user = request.COOKIES.get('username')
    if user:
        tc = models.Teacher.objects.get(id=selected)
        OpenMessages = models.LeaveWord.objects.filter(teacher=tc)

        NUM = 10
        index = []
        current = int(current)
        total = len(OpenMessages)
        pages = total / NUM
        if total % NUM != 0:
            pages += 1

        i = -2
        while i <= 2:
            if 1 <= current + i <= pages:
                index.append(current + i)
            i += 1

        first = [1]
        last = [pages]

        begin = (current - 1) * NUM
        end = min(NUM * current - 1, total - 1)
        begin = total - begin
        end = total - end
        show = []
        for i in range(begin - 1, end - 2, -1):
            show.append(OpenMessages[i])

        return render_to_response('Student/TeacherHomepage.html', {'current': current,
                                                          'index': index,
                                                          'teacher': teacher,
                                                          'first': first,
                                                          'last': last,
                                                          'openmessages': show,
                                                          'selected': selected,})
    else:
        return HttpResponseRedirect("/student/login/")


def tboard(request, selected, current):
    user = request.COOKIES.get('username')
    if user:
        tc = models.Teacher.objects.get(id=selected)
        usr = models.Student.objects.get(username=user)

        new = models.LeaveWord(
            teacher=tc,
            writer=usr,
        )

        if request.method == 'POST':
            new.content = request.POST.get('content')
            new.save()

        messages = models.LeaveWord.objects.filter(teacher=tc)

        NUM = 10
        index = []
        current = int(current)
        total = len(messages)
        pages = total / NUM
        if total % NUM != 0:
            pages += 1

        i = -2
        while i <= 2:
            if 1 <= current + i <= pages:
                index.append(current + i)
            i += 1

        first = [1]
        last = [pages]

        begin = (current - 1) * NUM
        end = min(NUM * current - 1, total - 1)
        begin = total - begin
        end = total - end
        show = []
        for i in range(begin - 1, end - 2, -1):
            show.append(messages[i])
        return render_to_response('Student/TeacherMessageBoard.html',{'current': current,
                                                              'selected': selected,
                                                              'index': index,
                                                              'teacher': teacher,
                                                              'first': first,
                                                              'last': last,
                                                              'new': new,
                                                              'messages': messages})
    else:
        return HttpResponseRedirect("/student/login")
