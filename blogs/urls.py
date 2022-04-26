"""URL patterns for blogs"""
from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    
    # blogs
    path('blogs', views.blogs, name='blogs'),
    path('edit', views.edit_blog, name='edit_blog'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
    
    # articles
    path('a/new', views.new_article, name='new_article'),
    path('a/<int:article_id>', views.article, name='article'),
]
