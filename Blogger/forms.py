from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))

    class Meta:
        model = Post
        fields = ['title', 'content']
