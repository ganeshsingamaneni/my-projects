from rest_framework.views import APIView
from onorapp.models import Users
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.forms.models import model_to_dict

class login(APIView):
    def post(self, request):
           """ auth """
           try:
               user =  self.request.data['emailId']
               obj = Users.objects.filter(emailId=user).first()
               if obj:
                   serializer = model_to_dict(obj)
                   is_valid = check_password(request.data['password'],serializer['password'])
                   if is_valid:
                       return JsonResponse({"success":True,"data":serializer,"message":'loggin successfully'})
                   return JsonResponse({"success":False, "message": 'username or password is incorrect'})
               return JsonResponse({"success":False, "message": 'username or password is incorrect'})
           except Exception as e:
               print(e)
               return JsonResponse({"success":False,"message": 'Internal server error'})
