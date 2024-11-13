from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Post, Comment
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa estar logado para comentar.')
            return self.get(request, *args, **kwargs)
        
        texto = request.POST.get('texto')
        if texto:
            Comment.objects.create(
                post=self.object,
                autor=request.user,
                texto=texto
            )
            messages.success(request, 'Comentário adicionado com sucesso!')
        else:
            messages.error(request, 'O comentário não pode estar vazio.')
        
        return self.get(request, *args, **kwargs)

class CriarPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/criar_post.html'
    success_url = reverse_lazy('lista_posts')

class EditarPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editar_post.html'
    success_url = reverse_lazy('lista_posts')

class RemoverPostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/remover_post.html'
    success_url = reverse_lazy('lista_posts')
    context_object_name = 'post'