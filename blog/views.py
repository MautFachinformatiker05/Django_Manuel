from django.shortcuts import render
from datetime import *
from .models import Post

posts =[
    {
        'author': 'MUnv',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': "July,18,2019"
    },
    {
        'author': 'OO',
        'title': 'Blog Post2',
        'content': 'second post content',
        'date_posted': "August,18,2019"
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    today= datetime.today()
    today=today.strftime("%B")
    return render(request, 'blog/about.html', {'date': today})
