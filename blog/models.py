from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='blogs')
    
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='blog-img/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)  # content
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField(help_text="Read time in minutes", default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    # update - like and dislike
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title if self.title else f"Blog {self.id}"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        
        if self.body:
            # Estimate read time (approx 200 words per minute)
            word_count = len(self.body.split())
            self.read_time = max(1, word_count // 200)
            
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
            
        super().save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    is_author_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - commented on {self.blog.title}"

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_likes')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blog', 'ip_address')
