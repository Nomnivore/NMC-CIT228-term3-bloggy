"""URL Patterns for users, inheriting from django auth"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # default auth urls
    path('', include('django.contrib.auth.urls')),

    # registration page
    path('register/', views.register, name='register'),
]
