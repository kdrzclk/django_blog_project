
from .models import Blog, Comment

from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = "__all__"
        exclude = ('user',) 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

