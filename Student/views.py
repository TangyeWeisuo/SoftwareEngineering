from django.shortcuts import render
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

