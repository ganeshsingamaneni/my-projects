from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Avg ,Max,Sum
from django.core import serializers
from itertools import chain
from django.http import JsonResponse
from DETAILS.models import StudentMarks, Subject
from django.http import HttpResponse, HttpResponseNotFound
import json

# MY views

#GETTING THE DATA OF EACH STUDENT
def studentdata(request):
    students = StudentMarks.objects.all() #each object in studentmarks table is assigned to students
    if students:
        context = {                    #it is a mapping that is passed to our template 'students.html'
            'students': students
        }
        return render(request, 'students.html', context) # render combines the given template with context and gives HttpResponse in given format in html syntax given in our html template
    else:
        return HttpResponseNotFound("student not found") #if no object is found with above condition then it will be displayed in the browser

# GETTING THE FACULTY DETAILS WITH NAME
def facultydata(request):
    faculty = Subject.objects.all()     #each object in subjects table is assingd to faculty
    if faculty:
        context = {                     #it is a mapping that is passed to our template 'students.html'
            'faculty': faculty
        }
        return render(request, 'students.html', context) # render combines the given template with context and gives HttpResponse in given format in html syntax given in our html template
    else:
        return HttpResponseNotFound("faculty not found")#if no object is found with above condtion then it will be displayed in the browser


#QUERY WITH  GIVEN PARAMETER AS ID FOR SEARCHING """
def getstudentid(request,_id):              #passing _id as parameter to the function
    print (_id) # it is to print in the terminal
    students = StudentMarks.objects.filter(id =_id) #based on given id the objects in StudentMarks are assigned to variable students
    if students:
        context = {                     #it is a mapping that is passed to our template 'students.html'
            'students': students
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")


#QUERY WITH FILTER FUNCTION FOR PARTICULAR SUBJECT
def getsubject(request,_subject): #passing one of the subject as the parameter
    #_subject = _subject.replace('%', ' ')

    students = StudentMarks.objects.filter(subject =_subject) #here we filter the objects by particular subject
    if students:
        context = {   #context maens a dictionary and mapping is done in our template "students.html"
            'students': students
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")



#QUERY WITH FILTER FUNCTION FOR PARTICULAR STUDENT
def getstudentname(request,_studentname): # here _studentname is the parameter to our FUNCTION
    _studentname = _studentname.replace('%', ' ')# the '%' replaces any ' - , _ ,  ' in our field names in the browser

    students = StudentMarks.objects.filter(student_name =_studentname)#here we filter the objects with particular studentname and assigned to variable students
    if students:
        context = {   #context means a dictionary and mapping is done in our template "students.html"
            'students': students
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")


#QUERY WITH GIVEN RANGE OF MARKS
def getrange(request,_range): # here _range is the parameter we are passing to the FUNCTION
    _range = _range.replace('%', ' ')# the '%' replaces any ' - , _ ,  ' in our field names in the browser
    start,end = [int(x) for x in _range.split('-')] # list comphrension for to define start and end values of range
    students = StudentMarks.objects.filter(Q(marks__gte=start)&Q(marks__lte=end))#here we filter the objects with given range of marks,where gte=greater than equal,lte=lessthanequal,Q is for  encapsulating the collection of keywords
    if students:
        context = {     #context means a dictionary and mapping is done in our template "students.html"
            'students': students
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")



#QUERY WITH PARTICULAR MARK
def getmarks(request,_marks):
    _marks = _marks.replace('%', ' ') # the '%' replaces any ' - , _ ,  ' in our field names in the browser

    students = StudentMarks.objects.filter(marks =_marks)#here the objects are filtered based on marks
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")

#QUERY FOR FINDING Mathematics SUBJECT TOPPER
def getmathstopper(request):
    max_rating = StudentMarks.objects.filter(subject="Mathematics").aggregate(Max('marks'))['marks__max']
    students = StudentMarks.objects.filter(marks = max_rating, subject="Mathematics")
    if students:
        context = {
            'students': students
        }
        return render(request, 'students.html', context)# render combines the given template with context and gives HttpResponse in given format in html
    else:
         return HttpResponseNotFound("student not found") #if no object is found with above condition it will be displayed in the browser
#FINDING THE TOTAL MARKS FOR EACH STUDENT
def gettotal(request):
    total = StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks'))#here we are annotating(getting the particular student
    #in all objects with same name ) the marks of each student in all subject and sum is used to adding the marks
    if total:
        context = {
            'total': total
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")

#QUERY TO FIND THE AVERAGE MARK FOR EACH SUBJECT
def geteachsubavg(request):
    subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks'))
    #here we are grouping the objects with  subject and the filtering with given subject as parameter and calculating the average marks for that subject
    if subaverage:
        context = {
            'subaverage':subaverage
        }
        return render(request,'students.html',context)
    else:
        return HttpResponseNotFound("student not found")

 #QUERY TO FIND THE  STUDENT WITH HIGHEST TOTAL
def gettopper(request):
    total = StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks')).order_by('total')[:1].reverse()
    #here we are grouping objects with studentname and calculating their total marks in all subjects and then odering by total and getting the topper
    if total:
        context = {
            'total': total
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")


#QUERY TO FIND THE AVERAGE MARK FOR EACH SUBJECT WITHOUT FAILURES
def getsubavg(request):
    subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40)).order_by('-total')
    #here we are grouping by subject ang getting the average marks for each subject when marks is greater than 40
    sub = subaverage.first()['subject']
    #here we are taking the subject with highest average and assigned it to sub
    fac=Subject.objects.get(name= subaverage.first()['subject'])
    #here we are getting the name of the faculty with highest average
    context = {'highest subject average faculty':{'subject':fac.name,'faculty':fac.faculty,'average':subaverage.first()['total']}}
    return JsonResponse(context)#here we are returning json response



#QUERY TO FIND THE FACULTY WITH BEST AVERAGE
def gethighsubavg(request):
    subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40)).order_by('total')[:1].reverse()
    if subaverage:
        context = {
            'subaverage': list(subaverage)#here list is used to change the format into json serializer
        }
        return JsonResponse(context)#here we are returning json response
    else:
        return HttpResponseNotFound("student not found")


#QUERY TO FIND THE STUDENT WITH LEAST TOTAL
def getleaststudent(request):
    total = StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks')).order_by('total')[:1]
    #here we are grouping by students and getting the sum of marks for each studnet and ordered by increasing order ang getting the first object through slicling
    if total:
        context = {
            'total': total
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")


#QUERY TO FIND THE STUDENTS WITH TOTAL MORE THAN 400
def getbeststudents(request):
    total = StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks')).filter(Q(total__gte=400))
    #here we are getting the students whose total greater than 400
    print(total)
    if total:
        context = {
            'total': total
        }
        return render(request, 'students.html', context)
    else:
        return HttpResponseNotFound("student not found")
