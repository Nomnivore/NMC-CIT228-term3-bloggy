from django import forms

from .models import Blog, Article


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'published']

