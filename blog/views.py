from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalhe_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/detalhe_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    
    return render(request, 'blog/criar_post.html', {'form': form})

def editar_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('lista_posts')
        else:
            form = PostForm(instance=post)
        
        return render(request, 'blog/editar_post.html', {'form': form, 'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")

def remover_post(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        
        if request.method == 'POST':
            post.delete()
            return redirect('lista_posts')
        
        return render(request, 'blog/remover_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")