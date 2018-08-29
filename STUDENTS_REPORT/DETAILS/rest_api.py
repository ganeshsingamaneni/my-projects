from rest_framework.decorators import api_view
from rest_framework.response import Response
from DETAILS.models import StudentMarks,Subject
from django.shortcuts import render
from django.core import serializers
from .serializers import StudentMarksSerializer,SubjectSerializer
from django.http import JsonResponse
from django.db.models import Q, Sum, Max, Count,Avg



#it's a test case
@api_view(['GET'])
def test(request):#it is our test case to know rest_framework is working or not
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})#it will return in json response

#getting each students marks with each subject
@api_view(['GET'])
def studentlist(request):
    students = StudentMarks.objects.all()#here all the objects are assigned to students
    if students:
        serial = StudentMarksSerializer(students,many=True)#taking the objects from StudentMarksSerializer and assigned them to serial variable
        return Response(serial.data)#it will return the response as json format

    else:
        return Response({"Message": 'STUDENTS NOT FOUND'})#it will return the response as json format


#getting students with particular mark
@api_view(['GET'])
def studentmarks(request,_marks): #taking marks as the parameter to the function
    _marks = _marks.replace('%', ' ')# the '%' replaces any ' - , _ ,  ' in our field names in the browser
    stud = StudentMarks.objects.filter(marks = _marks)#here objects are assingd to the variable  based on given marks
    if stud:
        serializer = StudentMarksSerializer(stud,many=True)#taking the objects from StudentMarksSerializer and assigned them to serializer variable
        return Response(serializer.data)#it will return the response as json format

    else:
        return Response({"Message": 'STUDENTS NOT FOUND'})#it will return the response as json format


#getting all the students with mathematics marks
@api_view(['GET'])
def single(request):
	s=StudentMarks.objects.filter(subject="Mathematics")#here objects are assigned to the variable based on subject 'mathematics'
	if s:
		serializer=StudentMarksSerializer(s,many=True)
		return Response(serializer.data)
	else:
		return HttpResponseNotFound("student not found")


#getting mathematics subject topper
@api_view(['GET'])
def mathstopper(request):
	s=StudentMarks.objects.filter(subject="Mathematics").order_by('-marks')[:1]
	#here objects are assigned to variable based on subject mathematics and ordered by marks in descending order and we are taking the first one by slicing
	if s:
		serializer=StudentMarksSerializer(s,many=True)
		return Response(serializer.data)
	else:
		return HttpResponseNotFound("no student")


#getting the students with marks more than 90 in each subject
@api_view(['GET'])
def ninty(request):
    students = StudentMarks.objects.filter(Q(marks__gte=90))
	#here objects are assigned to variable based on marks greater than or equal to 90
    if students:
        serializer = StudentMarksSerializer(students,many=True)
        return Response(serializer.data)
    else:
        return HttpResponseNotFound("student not found")



#finding the top faculty
@api_view(['GET'])
def topfaculty(request):
	students=StudentMarks.objects.all().values('subject').annotate(total=Count('student_name')).filter(Q(marks__gte=90)).order_by('-total')
    #here objects are assigned to variable by grouping with subject and we are counting how many are there for each subject with marks >90 and ordered by descending order
	count=students.first()['subject']
	# here we are taking first object from the above condition
	fac=Subject.objects.get(name=students.first()['subject'])
	#Subject is another model and we are taking the faculty based on the subject from the firstquery
	context={'faculty with more 90+ marks':{'subject':fac.name,'faculty':fac.faculty,'count':students.first()['total']}}
	return JsonResponse(context)


#finging the students total in all subjects
@api_view(['GET'])
def studentstotal(request):
	students=StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks'))
	#here objects are assigned to variable by grouping with student_name and calculating sum of marks for each student
	context={'students total marks':{
	          'students':list(students)
	}}
	return JsonResponse(context)


#finding the worst faculty
@api_view(['GET'])
def worstfaculty(request):
	subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=41)).order_by('total')
	#here objects are assinged to variable by grouping with subject and then we are calculating average for each subject when marks >=40,and ordering in descending order
	sub = subaverage.first()['subject']
	# here we are taking first object from the above condition
	fac=Subject.objects.get(name= subaverage.first()['subject'])
	#Subject is another model and we are taking the faculty based on the subject from the firstquery
	context = {'least subject average faculty':{'subject':fac.name,'faculty':fac.faculty,'average':subaverage.first()['total']}}
	return JsonResponse(context)


#finding each subject average by ignoring failures
@api_view(['GET'])
def eachsubavg(request):
	subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=41))
	#objects are grouped by subject where marks >=41  and calculating the average of marks for each subject
	print(subaverage)
	if subaverage:
		context={'each subject average ignoring failuers':{'subaverage':list(subaverage)}}
        return JsonResponse(context)


#finding the student with highest total
@api_view(['GET'])
def topstudent(request):
	#objects are grouped by student_name and calcultaing sum of marks of each student and ordered by descending order and taking the first object through slicling
	students=StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks')).order_by('-total')[:1]
	context={'student with highest total':{
	          'students':list(students)
	}}
	return JsonResponse(context)


#finding the student with least total
@api_view(['GET'])
def leaststudent(request):
	students=StudentMarks.objects.all().values('student_name').annotate(total=Sum('marks')).order_by('total')[:1]
	#objects are grouped by student_name and calcultaing sum of marks of each student and ordered by ascending order and taking the first object through slicling
	context={'student with lowest total':{
	          'students':list(students)
	}}
	return JsonResponse(context)



"""@api_view(['GET'])
def bestfaculty(request):
    subaverage = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40)).order_by('-total')
	sub=subaverage.first()['subject']
    fac=Subject.objects.get(name= subaverage.first()['subject'])
	#here objects are assinged to variable by grouping with subject and then we are calculating average for each subject when marks >=40,and ordering in descending order
	#Subject is another model and we are taking the faculty based on the subject from the firstquery
	# here we are taking first object from the above condition
    context = {'highest subject average faculty':{'subject':fac.name,'faculty':fac.faculty,'average':subaverage.first()['total']}}
    return JsonResponse(context)"""

#finding the best faculty
@api_view(['GET'])
def bestfaculty(request):
	subavg = StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40)).order_by('-total')
	sub = subavg.first()['subject']
	fac = Subject.objects.get(name=subavg.first()['subject'])
	context = {'faculty with highest subject average':{'subject': fac.name,'faculty': fac.faculty,'average':subavg.first()['total']}}
	return JsonResponse(context)
