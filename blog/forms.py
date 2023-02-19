from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms


# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    # Form fields
    class Meta:
        model = Comment
        fields = ('body',)


# Form for posts
class PostForm(forms.ModelForm):
    # Form fields
    class Meta:
        model = Post
        fields = [
            'title',
            'featured_image',
            'content'
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
