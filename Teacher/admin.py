from django.contrib import admin
from .models import *

# Register your models here.


class LabAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduction')
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('introduction', {'fields': ['introduction']}),
    ]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'password', 'email')
    fieldsets = [
        ('username', {'fields': ['username']}),
        ('name', {'fields': ['name']}),
        ('password', {'fields': ['password']}),
        ('email', {'fields': ['email']}),
        ('age', {'fields': ['age']}),
        ('gender', {'fields': ['gender']}),
        ('introduction', {'fields': ['introduction']}),
        ('lab', {'fields': ['lab']}),
        ('subject', {'fields': ['subject']}),
    ]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lab, LabAdmin)
