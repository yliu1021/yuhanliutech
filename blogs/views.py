from django.shortcuts import render

from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-published_date')
    return render(request, 'blogs.html', {
        'blogs': blogs
    })
