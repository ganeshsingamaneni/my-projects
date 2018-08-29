# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentMarks, Subject


# Register your models here.

class StudentMarksDetail(admin.ModelAdmin):
    list_display = ('student_name','subject','marks')
admin.site.register(StudentMarks,StudentMarksDetail)



class SubjectDetail(admin.ModelAdmin):
    list_display = ('name','faculty')
admin.site.register(Subject, SubjectDetail)
