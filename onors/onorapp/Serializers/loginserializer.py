from rest_framework import serializers
from onorapp.models import Users


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields= ('emailId','password')
