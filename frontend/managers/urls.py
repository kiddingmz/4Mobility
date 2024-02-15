from django.contrib import admin
from django.urls import path
from managers.views import index as managers_index


urlpatterns = [
    path('', managers_index, name='index'),
    path('map/', managers_index, name='map'),
]
