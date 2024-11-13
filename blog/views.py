from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class ListaPostsView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']

class DetalhePostView(DetailView):
    model = Post
    template_name = 'blog/detalhe_post.html'
    context_object_name = 'post'

class CriarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/criar_post.html'
    success_url = reverse_lazy('lista_posts')

class EditarPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editar_post.html'
    success_url = reverse_lazy('lista_posts')

class RemoverPostView(DeleteView):
    model = Post
    template_name = 'blog/remover_post.html'
    success_url = reverse_lazy('lista_posts')
    context_object_name = 'post'