from django.forms import ModelForm
from core.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'description', 'author',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
