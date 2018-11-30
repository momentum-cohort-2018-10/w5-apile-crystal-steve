# from django.contrib.auth.models import User
from django.contrib import admin
from core.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('author', 'title', 'url', 'description',)
    prepopulated_fields = {'slug': ('title',)}


# class CommentAdmin(admin.ModelAdmin):
#     model = Comment
#     list_display = (Post.title, User, 'comment',)


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
