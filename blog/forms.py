from django import forms
from .models import Blog, Author, Category, Comment
from ckeditor.widgets import CKEditorWidget

class CreateBlogForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # body = forms.CharField(
    #     widget=CKEditorWidget()  # WYSIWYG - What You See is What You Get..
    # )
    
    class Meta:
        model = Blog
        fields = ['author', 'category', 'title', 'image', 'body']

        

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