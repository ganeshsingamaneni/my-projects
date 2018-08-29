from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Registers
from onorapp.Serializers.RegistersSerializer import RegistersSerializers,GetRegistersSerializers
from django.http import Http404
from rest_framework import status

class getUpdateDeleteRegisters(APIView):
    def get_object(self,id):
        try:
            return Registers.objects.get(id=id)
        except:
            raise Http404
    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=GetRegistersSerializers(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"success":False,"message:":"Registers not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=RegistersSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"updated_data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"Registers data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return JsonResponse({"success":True,"message":"Registers data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"Registers data not deleted"})
