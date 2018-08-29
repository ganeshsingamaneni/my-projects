from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Registers,Users
from onorapp.Serializers.RegistersSerializer import RegistersSerializers,GetRegistersSerializers
from onorapp.mails.register_mail import register_mail
from onorapp.mails.admin_mail import admin_mail
from django.http import Http404
from rest_framework import status


class addRegisters(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Registers.objects.all()
            serializer=GetRegistersSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except Registers.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        try:
            serializer=RegistersSerializers(data=request.data)
            obj = Users.objects.all().filter(status=1).filter(role=1).first()
            if serializer.is_valid():
                serializer.save()
                mail_id=request.data['email']
                mail = register_mail.send(mail_id)
                mail_to_admin = admin_mail.send(obj.emailId)
                if(mail == 'success' and mail_to_admin == 'success'):
                    return JsonResponse({"success":True,"data":serializer.data})
                return JsonResponse({"success":True,"data":serializer.data})
            return Response(serializer.data)
        except Http404:
            return Response({"success":False,"message":"Registers data not added"})
