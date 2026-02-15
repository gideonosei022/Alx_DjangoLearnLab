from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your content here...', 'rows': 6}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'rows': 4
            })
        }


class PostForm(forms.ModelForm):

    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
