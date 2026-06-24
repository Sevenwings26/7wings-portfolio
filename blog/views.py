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
class BlogIndex(View):
    def get(self, request):  # method get 
        blogs = Blog.published.all().order_by('-published_at')  # Retrieve Latest published blogs
        context = {
            'blogs': blogs,
            # 'categories': categories
        }
        return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    # Increment views
    blog.views += 1
    blog.save(update_fields=['views'])
    
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
    blogs = Blog.published.all().order_by('-published_at')[:2]
    context = {
        'recent_blogs': blogs,
    }
    return render(request, 'blog/read_detail.html', context)
    

def create_blog(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)  # request.FILES is added for image upload
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('blog-site')
        else:
            print("Form is not valid", form.errors)
            return render(request, "blog/create_blog.html", {"form":form})
    else:
        form = CreateBlogForm() 
        return render(request, "blog/create_blog.html", {"form":form})


def update_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
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

def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    return redirect('blog-site')


    
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def post_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
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
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def like_blog(request, slug):
    from .models import Like
    blog = get_object_or_404(Blog, slug=slug)
    ip = get_client_ip(request)
    
    if not Like.objects.filter(blog=blog, ip_address=ip).exists():
        Like.objects.create(blog=blog, ip_address=ip)
        blog.likes += 1
        blog.save(update_fields=['likes'])
    
    return JsonResponse({'likes': blog.likes, 'dislikes': blog.dislikes})

def dislike_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    session_key = f"disliked_{blog.id}"
    
    if not request.session.get(session_key, False):
        blog.dislikes += 1
        blog.save(update_fields=['dislikes'])
        request.session[session_key] = True  # To prevent multiple dislikes
    
    return JsonResponse({'likes': blog.likes, 'dislikes': blog.dislikes})


import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decouple import config

# # Configure Gemini
# GOOGLE_API_KEY = config("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel('gemini-pro')

# @csrf_exempt
# def autocomplete_blog(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_input = data.get('prompt', '')
#         print("User input received:", user_input)

#         if not user_input:
#             return JsonResponse({'suggestion': ''})

#         # Improve prompt for Gemini
#         prompt = f"Continue this blog post with a plausible next phrase or sentence:\n\n{user_input}"

#         try:
#             response = model.generate_content(
#                 prompt,
#                 generation_config={
#                     'max_output_tokens': 20,
#                     'temperature': 0.7,
#                     'top_p': 1.0
#                 },
#                 stream=False,
#             )

#             suggestion = response.text.strip()
#             return JsonResponse({'suggestion': suggestion})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)
