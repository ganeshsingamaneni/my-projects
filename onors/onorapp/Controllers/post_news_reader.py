from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.Serializers.news_readerSerializer import newsReaderSerializers
from django.http import JsonResponse
from onorapp.models import newsReader
from django.http import Http404
from rest_framework import status

class addnewsreader(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=newsReader.objects.all()
            serializer=newsReaderSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except newsReader.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        try:
            serializer=newsReaderSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.data)
        except Http404:
            return Response({"success":False,"message":"news data not added"})
