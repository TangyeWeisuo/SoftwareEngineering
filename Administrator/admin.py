from django.contrib import admin
from .models import *


class StudentListAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'name', 'grade', 'gender')
    fieldsets = [
        ('studentID', {'fields': ['studentID']}),
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
        ('datetime', {'fields': ['datetime']}),

    ]


admin.site.register(StudentList, StudentListAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(OpenMessage, OpenMessageAdmin)
