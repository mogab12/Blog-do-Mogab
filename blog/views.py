from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    print("Número de posts:", posts.count())
    print("Posts:", list(posts.values('titulo', 'conteudo')))
    return render(request, 'blog/lista_posts.html', {'posts': posts})