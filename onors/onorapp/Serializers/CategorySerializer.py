from rest_framework import serializers
from onorapp.models import Categories
from onorapp.Serializers.UserSerializer import UserSerializers


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

class GetCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        depth = 2
        fields="__all__"
