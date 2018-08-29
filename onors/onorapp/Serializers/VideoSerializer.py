from rest_framework import serializers
from onorapp.models import Videos
#from onorapp.Serializers.RolesSerializer import RolesSerializers

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Videos
        fields="__all__"

class GetVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Videos
        depth = 2
        fields="__all__"
