from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Category, Blog, Comment, Tag, Like

# Register your models here.
admin.site.register(Author)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Tag, TagAdmin)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'created_at', 'published_at')
    list_filter = ('status', 'created_at', 'author', 'category')
    search_fields = ('title', 'body')
    
admin.site.register(Blog, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)
