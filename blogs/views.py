from django.shortcuts import render

# Create your views here.


def index(request):
    """The homepage for the app"""
    return render(request, 'blogs/index.html')
