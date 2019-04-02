from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import userSerializer
from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response


class Adduser(APIView):
    def get(self,request):
        # name = request.POST.get('name',none)
        # email = request.POSt.get('email',none)
        get=user.objects.all()
        serializer = userSerializer(get,many=True)
        if serializer:
            return JsonResponse({"success":True,"data":serializer.data})    
        return Response({"success":False})   


    def post(self,request):
        # get=user.objects.all()
        serializer=userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success":True,"data":serializer.data})
        return Response({"success":False})

