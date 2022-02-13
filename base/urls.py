from django.urls import path
from . import views

urlpatterns = [

    path ('tracks', views.getTracks, name='tracks'),
    path ('radio_shows', views.getPodcasts, name='podcasts'),
 
]