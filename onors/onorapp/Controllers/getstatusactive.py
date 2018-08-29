from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryCarousel,Users,Roles,Carousel,Categories
from onorapp.models import CategoryList,CategoryListImages,Videos
from onorapp.Serializers.CategorySerializer import CategoriesSerializers,GetCategoriesSerializers
from onorapp.Serializers.CategoryListimagesSerializer import GetCategoryListImageSerializers
from onorapp.Serializers.CarouselSerializer import CarouselSerializers,CarouselgetSerializers
from onorapp.Serializers.CategoryCarouselSerializer import GetCategoryCarouselSerializers
from onorapp.Serializers.UserSerializer import UserSerializers,UserroleSerializers
from onorapp.Serializers.CategoryListSerializer import GetCategoryListSerializers
from onorapp.Serializers.RolesSerializer import RolesSerializers
from onorapp.Serializers.VideoSerializer import GetVideoSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status


class getcategorystatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Categories.objects.all().filter(status=True)
            serializer=GetCategoriesSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "categories with active status nor found"})

class getuserstatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Users.objects.all().filter(status=True)
            serializer=UserroleSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "users with active status nor found"})

class getrolesstatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Roles.objects.all().filter(status=True)
            serializer=RolesSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "roles with active status nor found"})


class getcarouselstatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Carousel.objects.all().filter(status=True)
            serializer=CarouselgetSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "carousel with active status nor found"})

class getcategorycarouselstatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryCarousel.objects.all().filter(status=True)
            serializer=GetCategoryCarouselSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "categorycarousel with active status nor found"})

class getcategoryliststatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryList.objects.all().filter(status=True)
            serializer=GetCategoryListSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "categorylist with active status nor found"})


class getcategorylistimagestatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryListImages.objects.all().filter(status=True)
            serializer=GetCategoryListImageSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "categorylistimage with active status nor found"})


class getvideostatus(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Videos.objects.all().filter(status=True)
            serializer=GetVideoSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except:
            return JsonResponse({"success":False,"meaasge": "video with active status nor found"})
