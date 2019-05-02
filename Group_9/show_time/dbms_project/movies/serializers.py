from rest_framework import serializers
from movies.models import Movies, testmodel

# movie Serializer


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class TestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    genre = serializers.CharField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get(
            'genre', instance.genre)

        instance.save()
        return instance
