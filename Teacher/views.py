from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from Teacher.models import *
from SoftwareEngineering.settings import *
from Administrator.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
#from somewhere import handle_uploaded_file


# Create your views here.
def TeacherHomePage(request,current):
    if request.user.is_authenticated():
        print request.user.username
        teacher = Teacher.objects.get(username=request.user.username)
        OpenMessages = OpenMessage.objects.filter(writer = teacher)
        if request.method == 'POST':
            a = OpenMessage(content = request.POST.get('content'),
                            writer = teacher)
            a.save()
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
        return render_to_response('TeacherHomepage.html',{'current': current,
                                                          'index':index,
                                                          'teacher':teacher,
                                                          'first': first,
                                                          'last': last,
                                                          'openmessages':show})
    else:
        return HttpResponseRedirect("/TeacherLogIn/")


def TeacherInformation(request):
    if request.user.is_authenticated():
        teacher = Teacher.objects.get(username=request.user.username)
        return render_to_response('TeacherInformation.html',{'teacher':teacher})
    else:
        return HttpResponseRedirect("/TeacherLogIn/")

def TeacherSchedule(request):
    if request.user.is_authenticated():
        teacher = Teacher.objects.get(username=request.user.username)
        user=Student.objects.get(id=9999)
        if request.method == 'POST':
            pe = int(request.POST['pe'])
            day = pe % 7
            period = pe / 7
            if models.Agenda.objects.filter(day=day, period=period, student=user):
                return HttpResponse("Existed.")
            else:
                agd = models.Agenda(
                    teacher=teacher,
                    student=models.Student.objects.get(id=9999),
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
        selection = teacher
        items = models.Agenda.objects.filter(teacher=selection)

        for item in items:
            if item.student == super_student:
                table[item.period][item.day+1][0] = 2
            else:
                table[item.period][item.day+1][0] = 1

        return render_to_response('TeacherSchedule.html',{'teacher':teacher,'table':table})
    else:
        return HttpResponseRedirect("/TeacherLogIn/")
    
def TeacherMessageBoard(request,current):
    if request.user.is_authenticated():
        teacher = Teacher.objects.get(username=request.user.username)
        messages = LeaveWord.objects.filter(writer = teacher)
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
        return render_to_response('TeacherMessageBoard.html',{'current': current,
                                                              'index':index,
                                                              'teacher':teacher,
                                                              'first': first,
                                                              'last': last,
                                                              'messages':messages})
    else:
        return HttpResponseRedirect("/TeacherLogIn/")

def TeacherChangeInformation(request):
    if request.user.is_authenticated():
        teacher = Teacher.objects.get(username=request.user.username)
        if request.method == 'POST':
            if 'chooselab' in request.POST:
                return HttpResponseRedirect("/TeacherChooseLab/")
            s = request.POST.get('sex')
            if s == 'male':
                sex = False
            else:
                sex = True
            if 'email' in request.POST and request.POST.get('email')!='None':
                teacher.email = request.POST.get('email')
            if 'name' in request.POST:
                teacher.name = request.POST.get('name')
            if 'age' in request.POST and request.POST.get('age') != 'None':
                teacher.age = int(request.POST.get('age'))
            if 'gender' in request.POST:
                if request.POST.get('gender') == 'M':
                    teacher.gender = True
                else:
                    teacher.gender = False
            if 'introduction' in request.POST and request.POST.get('introduction')!='None':
                teacher.introduction = request.POST.get('introduction')
            if 'foundation' in request.POST and request.POST.get('foundation')!='None':
                teacher.foundation =  request.POST.get('foundation')
            if 'subject' in request.POST and request.POST.get('subject')!='None':
                teacher.subject = request.POST.get('subject')
            if 'photo' in request.FILES and request.FILES['photo']:
                #pic = request.POST.get('photo')
                #pic1 = Image.open(pic)
                print MEDIA_ROOT
                print request.FILES['photo'].name
                #file_content = ContentFile(request.FILES['photo'].read())
                teacher.photo=request.FILES['photo']
            #print a
            #print teacher.photo.path
            teacher.save()
        return render_to_response('TeacherChangeInformation.html',{'teacher':teacher})
    else:
        return HttpResponseRedirect("/TeacherLogIn/")
    
def TeacherLogIn(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            return HttpResponseRedirect("/TeacherRegister/")
        else:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            print username,password
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/TeacherHomePage/1/")
            else:
                # Show an error page
                return HttpResponse("failed")
    return render_to_response('TeacherLogIn.html')

def TeacherRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = request.POST.get('check')
        if password == check:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            teacher = Teacher(username=username,
                              password=password,
                              email=email)
            teacher.save()
            return HttpResponseRedirect('/TeacherLogIn/')
        else:
            return render_to_response('TeacherRegister.html')
    return render_to_response('TeacherRegister.html')

def TeacherChooseLab(request):
    if request.user.is_authenticated():
        teacher = Teacher.objects.get(username=request.user.username)
        lab_list=Lab.objects.filter()
        if request.method == 'POST':
            if 'choose' in request.POST:
                lab=Lab.objects.get(id=int(request.POST.get('choose')))
                teacher.lab=lab
                teacher.save()
        return render_to_response('LabChoose.html',locals())

def CreateLab(request):
    if request.method == 'POST':
        errors = []
        if not request.POST.get('name',''):
            errors.append("请输入实验室名称！")
        if not request.POST.get('introduction',''):
            errors.append("请输入实验室简介！")
        else:
            lab=Lab(name = request.POST.get('name'),
                    introduction = request.POST.get('introduction'))
            lab.save()
    return render_to_response('LabRigiser.html')

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/TeacherLogIn/")