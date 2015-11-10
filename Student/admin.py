from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    fieldsets = [
        ('username', {'fields': ['username']}),
        ('password', {'fields': ['password']}),
        ('email', {'fields': ['email']}),
    ]


admin.site.register(Student, StudentAdmin)
