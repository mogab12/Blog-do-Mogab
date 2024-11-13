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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_posts')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

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
        context['comentarios'] = self.object.comentarios.all().order_by('-data_postagem')
        context['form_comentario'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            return redirect('login')  # Redireciona para página de login

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = self.object
            comentario.save()
            return redirect('detalhe_post', pk=self.object.pk)

        # Se o formulário for inválido, renderiza novamente a página
        context = self.get_context_data()
        context['form_comentario'] = form
        return self.render_to_response(context)

class CriarPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/criar_post.html'
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editar_post.html'
    success_url = reverse_lazy('lista_posts')

    def get_queryset(self):
        # Permite edição apenas para o autor do post
        qs = super().get_queryset()
        return qs.filter(autor=self.request.user)

class RemoverPostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/remover_post.html'
    success_url = reverse_lazy('lista_posts')
    context_object_name = 'post'

    def get_queryset(self):
        # Permite remoção apenas para o autor do post
        qs = super().get_queryset()
        return qs.filter(autor=self.request.user)

class ListaCategoriasView(ListView):
    model = Category
    template_name = 'blog/lista_categorias.html'
    context_object_name = 'categorias'

class DetalheCategoriaView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem'] 

    def get_queryset(self):
        categoria = get_object_or_404(Category, pk=self.kwargs['pk'])
        return categoria.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context