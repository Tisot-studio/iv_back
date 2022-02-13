from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  *
from .serializers import *


@api_view (['GET'])
def getTracks(request):
    tracks = Release.objects.all()
    serializer = ReleaseSerializer(tracks, many=True)
    return Response (serializer.data)


@api_view (['GET'])
def getPodcasts(request):
    podcast = Podcast.objects.all()
    serializer = PodcastSerializer(podcast, many=True)
    return Response (serializer.data)