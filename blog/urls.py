from django.urls import path 
from . import views

urlpatterns = [
    path('site/', views.blog_index, name="blog-site"),
    path('read/<int:blog_id>/', views.blog_detail, name="blog_detail"),
    path('create/', views.create_blog, name="create-blog"),    
    path('update/<int:blog_id>', views.update_blog, name="update-blog"),    
    path('delete/<int:blog_id>', views.delete_blog, name="delete-blog"),    
]



