from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def base(request):
    return render(request, 'base.html',{})

def home(request):
    courses = Course.objects.all()
    blog = Blog.objects.order_by("-date")[:5]
    category_blog = Category_blog.objects.all()
    popular = Blog.objects.order_by('-popular')[:5]
    return render(request, 'home.html',{
        'courses':courses,
        'blog':blog,
        'category_blog':category_blog,
        'popular':popular
    })


def category(request , slug):
    category_blog = Category_blog.objects.all( )
    category = Category_blog.objects.get(slug=slug)
    blog = category.blog_set.order_by("-date")
    popular = Blog.objects.order_by('-popular')[:5]


    return render(request, 'category.html',{
        'category_blog':category_blog,
        'category':category , 
        'blog':blog,
        'popular':popular
    })


def single(request , pk):
    single = Blog.objects.get(id=pk)
    single.popular += 1
    single.save()
    blog = Blog.objects.filter(category_blog__title = single.category_blog)
    category_blog = Category_blog.objects.all( )
    popular = Blog.objects.order_by('-popular')[:5]

    return render(request, "single.html", {
        'single':single,
        'blog':blog,
        'category_blog':category_blog,
        'popular':popular
    })