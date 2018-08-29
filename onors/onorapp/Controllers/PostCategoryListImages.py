from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryListImages
from onorapp.Serializers.CategoryListimagesSerializer import CategoryListImageSerializers,GetCategoryListImageSerializers
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status

class createItemImages(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryListImages.objects.all()
            serializer=GetCategoryListImageSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except CategoryListImages.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoryListImageSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message":"ItemImages data not added"})
