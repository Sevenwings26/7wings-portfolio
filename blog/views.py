from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Author, Category
from .forms import CreateBlogForm


def blog_index(request):
    # blogs = Blog.objects.all().order_by('-created_at')  # 
    blogs = Blog.objects.all()  # 
    # categories = Category.objects.all()
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


def create_blog(request):
    form = CreateBlogForm()

    return render(request, 'blog/create_blog.html', {'form':form})

# @login_required
# def create_blog(request):
#     form = CreateBlogForm(request.POST, request.FILES)
#     if request.method == "POST":
#         if form.is_valid():
#             blog = form.save()
#             messages.success(request, "Blog created successfully!")
#             return redirect('blog_detail', pk=blog.pk)
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = CreateBlogForm()
    
#     return render(request, "blog/create.html", {"form": form})

# @login_required
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            updated_blog = form.save()
            messages.success(request, "Blog updated successfully!")
            return redirect('blog_detail', pk=updated_blog.pk)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CreateBlogForm(instance=blog)
    
    return render(request, 'blog/update.html', {'form': form, 'blog': blog})

# @login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog deleted successfully!")
        return redirect('blog_index')
    
    return render(request, 'blog/confirm_delete.html', {'blog': blog})

    