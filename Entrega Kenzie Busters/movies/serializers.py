from rest_framework import serializers
from .models import RatingChoice
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_blank=True,
        default="")
    rating = serializers.ChoiceField(
        choices=RatingChoice.choices,
        default=RatingChoice.G
    )
    synopsis = serializers.CharField(allow_blank=True, default="")
    added_by = serializers.EmailField(
        read_only=True,
        source="user.email"
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
