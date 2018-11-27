from django.contrib import admin
from core.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('author', 'title', 'url', 'description',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
