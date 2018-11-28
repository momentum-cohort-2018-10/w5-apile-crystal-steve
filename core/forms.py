from django.forms import ModelForm
from core.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'description', 'author',)


# * either create a new "create post form" or look at Clinton's forms that don't require classes
