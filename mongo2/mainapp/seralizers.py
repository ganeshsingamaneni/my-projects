from rest_framework_mongoengine import serializers


from .models import PollModel,ChoiceModel

class ChoiceModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ChoiceModel
        fields = '__all__'

class PollModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = PollModel
        fields = '__all__'
