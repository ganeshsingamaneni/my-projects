from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import Categories
from onorapp.Serializers.CategorySerializer import CategoriesSerializers,GetCategoriesSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addCategories(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Categories.objects.all()
            serializer=GetCategoriesSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except Categories.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoriesSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message":"Categories data not added"})
