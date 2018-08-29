from rest_framework import serializers
from onorapp.models import Carousel
from onorapp.Serializers.UserSerializer import UserSerializers


class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model=Carousel
        fields="__all__"#("id","slide","status","user","carouselname")


class CarouselgetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Carousel
        depth=2
        fields="__all__"
