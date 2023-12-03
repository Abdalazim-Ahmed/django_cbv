from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class Blog_List(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    ordering = ['-title']
    queryset = Blog.objects.filter(active=True)


class Blog_Detail(DetailView):
    model = Blog   