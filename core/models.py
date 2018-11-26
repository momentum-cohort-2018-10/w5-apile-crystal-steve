from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
            blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    url = models.URLField()
    description = models.CharField(max_length=255)

class Comment(models.Model):
    commenter = models.ForeignKey(to=User, on_delete=models.CASCADE,
            blank=True, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

class Vote(models.Model):
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE,
            blank=True, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'voter',
            'post',
        )
