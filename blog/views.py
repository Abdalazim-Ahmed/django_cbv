from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class Blog_List(ListView):
    model = Blog



class Blog_Detail(DetailView):
    model = Blog    