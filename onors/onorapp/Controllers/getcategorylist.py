from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryList
from onorapp.Serializers.CategoryListSerializer import CategoryListSerializers,GetCategoryListSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status





class getCategoryList(APIView):
   def get_object(self, id):
       try:
           return CategoryList.objects.filter(category=id)
       except:
           raise Http404
   def get(self, request, id, format=None):
       try:
           cat = self.get_object(id)
           serializer=GetCategoryListSerializers(cat,many=True)
           return JsonResponse({"success":True,"data":serializer.data})
       except Http404:
           return JsonResponse({"message:":"listings not found"})
