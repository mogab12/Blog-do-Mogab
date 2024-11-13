from django.contrib import admin
from .models import Post, Comment, Category

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('autor', 'post', 'data_postagem')
    list_filter = ('data_postagem', 'autor')
    search_fields = ('texto', 'autor__username', 'post__titulo')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

admin.site.register(Post)