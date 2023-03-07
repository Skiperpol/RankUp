from django.urls import path

from . import views
from backend.views import register, main, login_web, logout_view, profile, settings

urlpatterns = [
    path('main/', main, name='main'),
    path('login_web/', login_web, name='login_web'),
    path('register/', register, name='register'),

    path('logout/', logout_view, name='logout'),
    path('profile/<nick>', profile, name='profile'),
    path('settings', settings, name='settings'),
]