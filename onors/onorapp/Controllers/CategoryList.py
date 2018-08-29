from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryList
from onorapp.Serializers.CategoryListSerializer import CategoryListSerializers
from onorapp.Serializers.CategoryListSerializer import GetCategoryListSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class getUpdateDeleteCategoryList(APIView):
    def get_object(self,id):
        try:
            return CategoryList.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=GetCategoryListSerializers(get)
            return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"Categorylist not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=CategoryListSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"Categorylist data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"success":True,"message":" Categorylist data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"Categorylist data not deleted"})
