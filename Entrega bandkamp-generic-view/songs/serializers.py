from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "duration",
            "album_id"
        ]
