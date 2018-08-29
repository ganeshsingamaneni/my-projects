from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.Serializers.CarouselSerializer import CarouselSerializers
from onorapp.Serializers.CarouselSerializer import CarouselgetSerializers
from django.http import JsonResponse
from onorapp.models import Carousel
from django.http import Http404
from rest_framework import status

class addCarousel(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Carousel.objects.all()
            serializer=CarouselgetSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except Carousel.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        try:
            serializer=CarouselSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.data)
        except Http404:
            return Response({"success":False,"message":"Carousel data not added"})
