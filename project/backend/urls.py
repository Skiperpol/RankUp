from django.urls import path
from backend.views import main

urlpatterns = [
    path('main/', main, name='main'),
]