from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField  

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name

    # def get_absolute_url(self):
    #     return reverse('author_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    admin_author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)   # use later
    author = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='blog-img/', blank=True, null=True)
    # body = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    # on_delete=models.CASCADE - if deleting the author, django will auto delete the author's blog posts on delete of author

    # on_delete=models.PROTECT - if deleting the author, django will not delete the author if the author has blogs.

    # on_delete=models.SET_NULL - if deleting the author, django will make the author column as blank.

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
