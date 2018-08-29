from rest_framework import serializers
from onorapp.models import Roles

class RolesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields="__all__"
