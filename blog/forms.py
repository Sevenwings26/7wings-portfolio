from django import forms
from .models import Blog, Author, Category, Comment

class CreateBlogForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    admin_author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # title = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )

    # body = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    # )
    
    class Meta:
        model = Blog
        fields = ['admin_author', 'author', 'category', 'title', 'image', 'body']

        
        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'form-control'}),
        # }



# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'content']
#         widgets = {
#             'content': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 3,
#                 'placeholder': 'Write your comment here...'
#             }),
#         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
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