from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.Serializers.news_readerSerializer import newsReaderSerializers
from django.http import JsonResponse
from onorapp.models import newsReader
from django.http import Http404
from rest_framework import status


class getUpdateDeletenewsreader(APIView):
    def get_object(self,id):
        try:
            return newsReader.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=newsReaderSerializers(get)
            return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"NewsReader not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=newsReaderSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"NewsReader data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"success":True,"message":" NewsReader data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"NewsReader data not deleted"})
