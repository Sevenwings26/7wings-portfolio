from django.urls import path 
from . import views

urlpatterns = [
    path('site/', views.blog_index, name="blog-site"),
    path('read/<int:blog_id>/', views.blog_detail, name="blog_detail"),
    path('create/', views.create_blog, name="create-blog"),    
    path('update/<int:blog_id>', views.update_blog, name="update-blog"),    
    path('delete/<int:blog_id>', views.delete_blog, name="delete-blog"), 

    # comment, likes
    # path('post-comment/<int:post_id>', views.post_comment, name="post_comment"), 
    path('<int:blog_id>/comment/', views.post_comment, name='post_comment'),
    path('post/<int:comment_id>/reply/', views.post_reply, name='post_reply'),
    path('/post/<int:blog_id>/like/', views.like_blog, name='like_blog'),
    path('post/<int:blog_id>/dislike/', views.dislike_blog, name='like_blog'),
]



