from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryCarousel
from onorapp.Serializers.CategoryCarouselSerializer import CategoryCarouselSerializers,GetCategoryCarouselSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addCategoryCarousel(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryCarousel.objects.all()
            serializer=GetCategoryCarouselSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except CategoryCarousel.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        try:
            serializer=CategoryCarouselSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message":"CategoryCarousel data not added"})
