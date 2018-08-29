from rest_framework import serializers
from onorapp.models import CategoryListImages
from onorapp.Serializers.UserSerializer import UserSerializers
from onorapp.Serializers.CategoryListSerializer import CategoryListSerializers


class CategoryListImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryListImages
        fields="__all__"

class GetCategoryListImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryListImages
        depth = 2
        fields="__all__"
