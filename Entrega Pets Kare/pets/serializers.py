from rest_framework import serializers
from .models import SexChoice
from groups.serializers import GroupsSerializer
from traits.serializers import TraitsSerializer


class PetsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexChoice.choices, default=SexChoice.Not_Informed)
    group = GroupsSerializer()
    traits = TraitsSerializer(many=True)
