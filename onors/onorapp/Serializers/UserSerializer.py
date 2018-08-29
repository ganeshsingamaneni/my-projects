from rest_framework import serializers
from onorapp.models import Users
from onorapp.Serializers.RolesSerializer import RolesSerializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"

class UserroleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        depth = 2
        fields="__all__"

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('emailId','password')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('first_name','last_name','mobile_no','address','emailId','status','role')
