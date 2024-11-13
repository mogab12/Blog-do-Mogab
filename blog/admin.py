from django.contrib import admin
from .models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('autor', 'post', 'data_postagem')
    list_filter = ('data_postagem', 'autor')
    search_fields = ('texto', 'autor__username', 'post__titulo')
admin.site.register(Post)