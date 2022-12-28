from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))

    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"row":"5"}))

    class Meta:
        model = Comment
        fields = ['content']