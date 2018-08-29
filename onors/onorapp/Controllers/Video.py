from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import Videos
from onorapp.Serializers.VideoSerializer import VideoSerializers
from onorapp.Serializers.VideoSerializer import GetVideoSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class getUpdateDeleteVideos(APIView):
    def get_object(self,id):
        try:
            return Videos.objects.get(id=id)
        except:
            raise Http404
    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=GetVideoSerializers(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"success":False,"message:":"Videos not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=VideoSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"updated_data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"Videos data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return JsonResponse({"success":True,"message":"Video data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"Video data not deleted"})
