from rest_framework import serializers

from musicapp.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model= Song
        fields=["title", "date_released", "likes", "artiste_id"]
