from django.shortcuts import render
from blog.models import Category, Post


def home(request):
    posts = Post.objects.all()   
    categories  = Category.objects.all() 
    context = {
            'posts': posts ,
            'categories': categories 
        }
    
    return  render(request, 'index.html', context)
