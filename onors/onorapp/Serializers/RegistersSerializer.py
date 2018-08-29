from rest_framework import serializers
from onorapp.models import Registers

class RegistersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Registers
        fields="__all__"

class GetRegistersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Registers
        depth = 1
        fields="__all__"
