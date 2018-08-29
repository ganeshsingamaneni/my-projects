from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryList
from onorapp.Serializers.CategoryListSerializer import CategoryListSerializers,GetCategoryListSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addCategoryList(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryList.objects.all()
            serializer=GetCategoryListSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except CategoryList.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoryListSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"CategoryList not added"})
