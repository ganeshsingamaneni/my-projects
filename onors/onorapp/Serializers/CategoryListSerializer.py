from rest_framework import serializers
from onorapp.models import CategoryList
from onorapp.Serializers.UserSerializer import UserSerializers
from onorapp.Serializers.CategorySerializer import CategoriesSerializers


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryList
        fields="__all__"

class GetCategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryList
        depth = 2
        fields="__all__"
