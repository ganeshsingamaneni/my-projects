from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Roles
from onorapp.Serializers.RolesSerializer import RolesSerializers
from django.http import Http404
from rest_framework import status

class getUpdateRoles(APIView):
    def get_object(self,id):
        try:
            return Roles.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=RolesSerializers(get)
            return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"Roles not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=RolesSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"success":False,"message":"Roles data not updated"})
