from django.urls import path 
from . import views

urlpatterns = [
    path('site/', views.blog_index, name="blog-site"),
    path('read/<int:blog_id>/', views.blog_detail, name="blog_detail"),
    path('create/', views.create_blog, name="create-blog"),    
]



