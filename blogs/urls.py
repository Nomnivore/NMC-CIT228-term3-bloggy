"""URL patterns for blogs"""
from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
]
