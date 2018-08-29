from rest_framework import serializers
from onorapp.models import newsReader



class newsReaderSerializers(serializers.ModelSerializer):
    class Meta:
        model=newsReader
        fields="__all__"
