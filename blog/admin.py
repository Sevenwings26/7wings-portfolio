from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Category, Blog, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)


# @admin.register(Blog)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
admin.site.register(Blog, PostAdmin)

admin.site.register(Comment)
