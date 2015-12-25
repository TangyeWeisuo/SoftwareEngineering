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


def welcome(request):
    return render_to_response('Student/welcome.html')