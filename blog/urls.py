from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.Blog_List.as_view(), name='blog_list'),
    path('detail/<int:pk>/', views.Blog_Detail.as_view(), name='blog_detail'),
]