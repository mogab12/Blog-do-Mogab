from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post

# Listar Posts
def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

# Detalhe do Post
def detalhe_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/detalhe_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")

# Criar Post
def criar_post(request):
    if request.method == 'POST':
        # Criação direta sem validação
        Post.objects.create(
            titulo=request.POST.get('titulo', ''),
            conteudo=request.POST.get('conteudo', '')
        )
        return redirect('lista_posts')
    
    return render(request, 'blog/criar_post.html')

# Editar Post
def editar_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        
        if request.method == 'POST':
            # Atualização direta sem validação
            post.titulo = request.POST.get('titulo', post.titulo)
            post.conteudo = request.POST.get('conteudo', post.conteudo)
            post.save()
            return redirect('lista_posts')
        
        return render(request, 'blog/editar_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")

# Remover Post
def remover_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        
        if request.method == 'POST':
            post.delete()
            return redirect('lista_posts')
        
        return render(request, 'blog/remover_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")