from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import Categories
from onorapp.Serializers.CategorySerializer import CategoriesSerializers
from onorapp.Serializers.CategorySerializer import GetCategoriesSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class getUpdateDeleteCategories(APIView):
    def get_object(self,id):
        try:
            return Categories.objects.get(id=id)
        except:
            raise Http404
    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=GetCategoriesSerializers(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"success":False,"message:":"Categories not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=CategoriesSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"updated_data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"Categories data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return JsonResponse({"success":True,"message":"Categories data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"Categories data not deleted"})
