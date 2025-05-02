from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Author, Category, Comment
from .forms import CreateBlogForm, CommentForm


def blog_index(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Retrieve Latest blog
    context = {
        'blogs': blogs,
        # 'categories': categories
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.all()
    # post comment 
    form = CommentForm(request.POST)
    if request.method == "POST" and request.headers.get('x-requested-with') == "XMLHttpRequest":
        if form.is_valid():
            comment = form.save(commit=True)
            comment.blog = blog
            comment.save()
            return JsonResponse({
                'name':comment.name,
                'content':comment.content,
                'created-at':comment.created_at.strftime('%b %d, %Y %H:%M')
            })
    context = {
        'blog': blog,
        'form':form,
        'comments':comments,
    }
    return render(request, 'blog/read_detail.html', context)


def post_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        # comment.author = request.user
        comment.save()
        
        return JsonResponse({
            'success': True,
            'comment_id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
            'created_at': comment.created_at.strftime("%B %d, %Y, %I:%M %p"),
            'avatar_url': comment.author.profile.avatar.url if hasattr(comment.author, 'profile') else '/static/images/default-avatar.jpg',
        })
    
    return JsonResponse({'success': False, 'errors': form.errors})




def recent_blogs(request):
    blogs = Blog.objects.all()[:2]
    context = {
        'recent_blogs': blogs,
    }
    return render(request, 'blog/read_detail.html', context)


def create_blog(request):
    form = CreateBlogForm(request.POST, request.FILES)  # request.FILES is added for image upload
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('blog-site')
        else:
            print("Form is not valid", form.errors)
            return render(request, "blog/create_blog.html", {"form":form})
    else:
        # form = CreateBlogForm() 
        return render(request, "blog/create_blog.html", {"form":form})


def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            print("Form Updated")
            return redirect('blog-site')
    else:     # GET http request
        form = CreateBlogForm(instance=blog) 
        return render(request, "blog/update_blog.html", {"form":form})



# @login_required

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('blog-site')


    