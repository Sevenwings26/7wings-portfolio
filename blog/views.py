from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Author, Category
from .forms import CreateBlogForm


def blog_index(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Retrieve Latest blog
    context = {
        'blogs': blogs,
        # 'categories': categories
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/read_detail.html', context)


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


    