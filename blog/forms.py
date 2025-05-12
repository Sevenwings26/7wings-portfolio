from django import forms
from .models import Blog, Author, Category, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Blog creation form 
class CreateBlogForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())  #  WYSIWYG - What You See is What You Get..
 
    class Meta:
        model = Blog
        fields = ['author', 'category', 'title', 'image', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
# Comment form 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'Name...'
            }),
            
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }

# Reply form                                       
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Write your reply here...'
            }),
        }
