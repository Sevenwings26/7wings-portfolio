from django.urls import path 
from . import views
from .autocomplete import autocomplete_blog

# from .views import BlogIndex

urlpatterns = [
    path('site/', views.BlogIndex.as_view(), name="blog-site"),
    path('read/<slug:slug>/', views.blog_detail, name="blog_detail"),
    path('create/', views.create_blog, name="create-blog"),    
    path('update/<slug:slug>', views.update_blog, name="update-blog"),    
    path('delete/<slug:slug>', views.delete_blog, name="delete-blog"), 

    # comment, likes
    # path('post-comment/<int:post_id>', views.post_comment, name="post_comment"), 
    path('<slug:slug>/comment/', views.post_comment, name='post_comment'),
    path('post/<int:comment_id>/reply/', views.post_reply, name='post_reply'),
    path('post/<slug:slug>/like/', views.like_blog, name='like_blog'),
    path('post/<slug:slug>/dislike/', views.dislike_blog, name='dislike_blog'),
    
    # autocomplete 
    # path('autocomplete/api/', views.autocomplete_blog, name='autocomplete_blog'),
    # path('autocomplete/api/', autocomplete_blog, name='autocomplete_blog'),
]



