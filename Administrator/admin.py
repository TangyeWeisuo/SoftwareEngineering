from django.contrib import admin
from .models import *


class StudentListAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'grade', 'gender')
    fieldsets = [
        ('ID', {'fields': ['ID']}),
        ('name', {'fields': ['name']}),
        ('grade', {'fields': ['grade']}),
        ('gender', {'fields': ['gender']}),
    ]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'content')
    fieldsets = [
        ('teacher', {'fields': ['teacher']}),
        ('student', {'fields': ['student']}),
        ('content', {'fields': ['content']}),
    ]


class OpenMessageAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'content')
    fieldsets = [
        ('teacher', {'fields': ['teacher']}),
        ('content', {'fields': ['content']}),
    ]


admin.site.register(StudentList, StudentListAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(OpenMessage, OpenMessageAdmin)
