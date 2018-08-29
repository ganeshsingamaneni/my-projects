# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import square
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from .serializers import squareSerializer



@api_view(['GET'])
def getsquare(request,_num):
    _num = _num.replace('%', ' ')
    sqr=square.objects.filter(number=_num)
    if sqr:
		serializer=squareSerializer(sqr,many=True)
		return Response(serializer.data)
    else:
        return Response({"Message": 'NUMBER NOT FOUND'})


@api_view(['POST'])
def postdata(request):
    number = request.POST.get("number",none)
    sqr = request.POST.get("sqr",none)
    squ=square.objects.create(number=number,sqr=sqr)
    return Response({'message': 'numsqr {:d} created'.format(squ.id)}, status=301)




@api_view(['GET', 'POST', 'PUT','DELETE'])
def post (request,_Number):

    if request.method == 'GET':
        mul = square.objects.filter(number=_Number)
        serializer = squareSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = squareSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= 301)

    elif request.method == 'PUT':
        print (request.data)
        mul = square.objects.filter(number=request.data["number"])
        print (mul)
        mul.update(sqr=request.data["sqr"])
        serializer = squareSerializer(data=mul, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)
    elif request.method == 'DELETE':
        mul = square.objects.filter(number=_Number)
        mul.delete()
        serializer = squareSerializer(data=mul, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 301)
