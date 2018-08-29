from rest_framework import serializers
from .models import square


class squareSerializer(serializers.ModelSerializer):
    class Meta:
        model = square
        fields = ('number','sqr')
