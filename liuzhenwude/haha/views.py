from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from haha.models import Enter
from haha.models import Student


def login(request):
    return render_to_response("login.html")

def apd(request):
    return render_to_response("register.html")

def append(request):
    if request.POST:
        post = request.POST
        Password = post["password"]
        Repassword = post["repassword"]
        if Password == Repassword:

            enter = Enter(
            studentnumber  =post["studentnumber"],
            email =post["email"],
            password = post["password"])
            enter.save()
            return render_to_response("success.html")
        else:
            return render_to_response("login.html")

def enterin(request):
    if request.POST:
        post = request.POST
        studentnumber = post['studentnumber']
        password = post['password']
        try:
            enteri = Enter.objects.filter(studentnumber=studentnumber)[0]
            print enteri.studentnumber
            print enteri.password
            rpassword=enteri.password
            if password == rpassword:
                #student = Student.objects.filter(username = studentnumber)
                return render_to_response('success.html')#,{'Student': student})
        except:
                 return render_to_response("failed.html")






