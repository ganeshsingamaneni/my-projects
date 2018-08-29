from rest_framework import serializers
from onorapp.models import CategoryCarousel
from onorapp.Serializers.UserSerializer import UserSerializers
from onorapp.Serializers.CategorySerializer import CategoriesSerializers



class CategoryCarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryCarousel
        fields="__all__"


class GetCategoryCarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=CategoryCarousel
        depth = 2
        fields="__all__"
