from django.contrib import admin
from django.urls import path
from managers.views import index as managers_index
from managers.views import map as managers_map


urlpatterns = [
    path('', managers_index, name='Dashboard'),
    path('map/', managers_map, name='Map'),
]
