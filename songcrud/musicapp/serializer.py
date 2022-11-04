from rest_framework import serializers

from musicapp.models import Song, Lyric


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model= Song
        fields=["title", "date_released", "likes", "artiste_id"]

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lyric
        fields=["content", "song_id"]

