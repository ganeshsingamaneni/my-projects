from rest_framework import serializers
from .models import StudentMarks,Subject

#here we are translating our models into serializers


class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = ('student_name', 'subject', 'marks')



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name','faculty')
