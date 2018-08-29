from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryCarousel,Categories
from onorapp.Serializers.CategoryCarouselSerializer import CategoryCarouselSerializers
from onorapp.Serializers.CategoryCarouselSerializer import GetCategoryCarouselSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status



class CategoryCarouselstatus(APIView):
  def get_object(self, id):
      try:
          if(Categories.objects.filter(id=id).filter(status=True)):
              return CategoryCarousel.objects.filter(category=id).filter(status=True)
      except:
          return JsonResponse({"success":True,"data":None,"message":"no data found with this id "})

  def get(self, request, id, format=None):
      try:
          cat = self.get_object(id)
          serializer = GetCategoryCarouselSerializers(cat,many=True)
          if serializer:
              return JsonResponse({"success":True,"data":serializer.data})
          return JsonResponse({"success":True,"data":None,"message":"no data found with this id "})
      except:
          return JsonResponse({"message:":"category_carousel  not found"})
