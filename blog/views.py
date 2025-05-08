from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Author, Category, Comment
from .forms import CreateBlogForm, CommentForm, ReplyForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.views.generic import TemplateView, ListView  
from django.views import View


# Class-based views
class BlogIndex(TemplateView):
    template_name = "blog/index.html"

class BlogIndex(View):
    def get(self, request):  # method get
        blogs = Blog.objects.all().order_by('-created_at')  # Retrieve Latest blog
        context = {
            'blogs': blogs,
            # 'categories': categories
        }
        return render(request, 'blog/index.html', context)



# def blog_index(request):
#     blogs = Blog.objects.all().order_by('-created_at')  # Retrieve Latest blog
#     context = {
#         'blogs': blogs,
#         # 'categories': categories
#     }
#     return render(request, 'blog/index.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog, parent__isnull=True)

    # forms 
    comment_form = CommentForm()
    reply_form = ReplyForm()

    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
        'reply_form': reply_form,
        # 'like_count': blog.likes.count()
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


    
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def post_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        
        return JsonResponse({
            'success': True,
            'comment_id': comment.id,
            'name': comment.name,
            'content': comment.content,
            'created_at': comment.created_at.strftime("%B %d, %Y, %I:%M %p"),
            'is_reply': False,
        })
    return JsonResponse({'success': False, 'errors': form.errors})



@csrf_exempt  # or use @csrf_protect + pass CSRF in JS
def post_reply(request, comment_id):
    if request.method == 'POST':
        parent = get_object_or_404(Comment, id=comment_id)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.parent = parent
            reply.blog = parent.blog
            # If you want to include the user's name, set it here
            # reply.name = request.user.username if request.user.is_authenticated else 'Anonymous'
            reply.save()

            return JsonResponse({
                'success': True,
                'comment_id': reply.id,
                'name': reply.name or 'Anonymous',
                'content': reply.content,
                'created_at': reply.created_at.strftime('%Y-%m-%d %H:%M'),
                'is_author_reply': False
            })
    return JsonResponse({'success': False}, status=400)

# likes and dislike  
# avoid for @csrf_exempt
def like_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    session_key = f"liked_{blog_id}"
    
    if not request.session.get(session_key, False):
        blog.likes += 1
        blog.save()
        request.session[session_key] = True  # To prevent multiple likes
    
    return JsonResponse({'likes': blog.likes, 'dislikes': blog.dislikes})

def dislike_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    session_key = f"liked_{blog_id}"
    
    if not request.session.get(session_key, False):
        blog.likes += 1
        blog.save()
        request.session[session_key] = True  # To prevent multiple likes
    
    return JsonResponse({'likes': blog.likes, 'dislikes': blog.dislikes})

