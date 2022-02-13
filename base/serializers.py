from dataclasses import fields
from rest_framework import serializers
from .models import *


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('spotify', 'beatport', 'itunes', 'soundcloud',)


class ReleaseSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Release
        fields = '__all__'
    
    def get_links(self, obj):
        items = obj.link
        serializer = LinkSerializer(items, many=False)
        return serializer.data


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'










