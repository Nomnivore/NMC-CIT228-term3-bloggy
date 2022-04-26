from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Blog, Article
from .forms import BlogForm, ArticleForm

# Create your views here.


def index(request):
    """The homepage for the app"""
    if request.user.is_authenticated:
        return render(request, 'blogs/index.html')
    else:
        return render(request, 'blogs/landing.html')


@login_required
def edit_blog(request):
    """Edit blog details like name, description"""
    blog = Blog.objects.get(user=request.user)

    if request.method != 'POST':
        # GET request, pre-fill form with current details
        form = BlogForm(instance=blog)
    else:
        # data submitted, process data
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    # render form on GET and invalid POST
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/edit.html', context)


def blog(request, blog_id):
    """Show a single blog and all of its articles"""
    blog = get_object_or_404(Blog, id=blog_id)

    # we need to check for ownership because drafts
    # should only be shown to the author
    if request.user == blog.user:
        articles = blog.article_set.all()
    else:
        articles = blog.published_set()

    context = {'blog': blog, 'articles': articles}
    return render(request, 'blogs/blog.html', context)


def blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


@login_required
def new_article(request):
    """Create a new article"""
    blog = Blog.objects.get(user=request.user)

    if request.method != 'POST':
        # GET request, pre-fill form with current details
        form = ArticleForm()
    else:
        # data submitted, process data
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.blog = blog
            article.save()
            return redirect('blogs:article', article_id=article.id)

    # render form on GET and invalid POST
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_article.html', context)


def article(request, article_id):
    """Show a single article"""
    article = get_object_or_404(Article, id=article_id)

    if not article.published:
        # it's a draft, only show it to the author
        if not request.user.is_authenticated or request.user != article.blog.user:
            raise Http404

    context = {'article': article}
    return render(request, 'blogs/article.html', context)

def edit_article(request, article_id):
    """Edit a single article"""
    article = get_object_or_404(Article, id=article_id)
    
    if not request.user == article.blog.user:
        raise Http404
    
    if request.method != 'POST':
        # GET request, pre-fill form with current details
        form = ArticleForm(instance=article)
    else:
        # data submitted, process data
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:article', article_id=article.id)
    
    context = {'form': form, 'article': article}
    return render(request, 'blogs/edit_article.html', context)
