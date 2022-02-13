from dataclasses import fields
from rest_framework import serializers
from .models import *


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class ReleaseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Release
        fields = '__all__'
    
    def get_links(self, obj):
        links = LinkSerializer(obj.links, many=False).data
        return links


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'










