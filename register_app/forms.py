from django import forms
from .models import Post, Comment
from django.utils.text import slugify


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'publish_date', 'author')

    def save(self):
        instance = super(PostForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
