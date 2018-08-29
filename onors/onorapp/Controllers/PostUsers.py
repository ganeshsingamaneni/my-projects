from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Users
from onorapp.Serializers.UserSerializer import UserSerializers,UserroleSerializers
from onorapp.mails.send_mail import SendMail
from django.http import Http404
from rest_framework import status
import crypt
from django.contrib.auth.hashers import make_password,check_password

class addUsers(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Users.objects.all()
            serializer=UserroleSerializers(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except Users.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=UserSerializers(data=request.data)
            role = request.data['role']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            mobile_no = request.data['mobile_no']
            address =  request.data['address']
            emailId = request.data['emailId']
            password = make_password(request.data['password'])
            status = request.data['status']
            users={"role":role,"first_name":first_name,"last_name":last_name,"mobile_no":mobile_no,"address":address,"emailId":emailId,"password":password,"status":status}
            serializer=UserSerializers(data=users)
            if serializer.is_valid():
                serializer.save()
                mail_id=request.data['emailId']
                mail = SendMail.send(mail_id)
                if(mail == 'success'):
                    return Response(serializer.data)
                return Response(serializer.data,status=301)
            #return Response(serializer.data)
        except Http404:
            return JsonResponse({"success":False,"message":"data not added"})
