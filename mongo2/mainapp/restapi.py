from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.core import serializers
from .seralizers import ChoiceModelSerializer,PollModelSerializer
from .models import ChoiceModel,PollModel
from django.http import JsonResponse


@api_view(['GET'])
def getapi(request):
	x= PollModel.objects.all()
	if x:
		serializer =PollModelSerializer(x, many=True)
		return Response(serializer.data)
	else:
		return Response({"Message": 'data Not Foud'})


@api_view(['GET', 'POST', 'PUT','DELETE'])
def post(request,_question):
    if request.method == 'GET':
        mul = PollModel.objects.filter(question=_question)
        serializer = PollModelSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PollModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)

    elif request.method == 'PUT':
        print (request.data)
        mul =PollModel.objects.filter(question=request.data["question"])
        print (mul)
        mul.update(question=request.data["question"])
        serializer = PollModelSerializer(data=mul, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)

    elif request.method=='DELETE':
        mul = PollModel.objects.filter(question=_question)
        mul.delete()
        serializer = PollModelSerializer(data=mul, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)
