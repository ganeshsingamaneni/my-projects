from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import Videos
from onorapp.Serializers.VideoSerializer import VideoSerializers,GetVideoSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addVideos(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Videos.objects.all()
            serializer=GetVideoSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except Videos.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=VideoSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"Video not added"})
