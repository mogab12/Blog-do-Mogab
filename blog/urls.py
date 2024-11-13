from django.urls import path
from .views import (
    ListaPostsView, 
    DetalhePostView, 
    CriarPostView, 
    EditarPostView, 
    RemoverPostView,
    ListaCategoriasView,
    DetalheCategoriaView,
    register
)

urlpatterns = [
    path('', ListaPostsView.as_view(), name='lista_posts'),
    path('post/<int:pk>/', DetalhePostView.as_view(), name='detalhe_post'),
    path('post/criar/', CriarPostView.as_view(), name='criar_post'),
    path('post/<int:pk>/editar/', EditarPostView.as_view(), name='editar_post'),
    path('post/<int:pk>/remover/', RemoverPostView.as_view(), name='remover_post'),
    path('categorias/', ListaCategoriasView.as_view(), name='lista_categorias'),
    path('categoria/<int:pk>/', DetalheCategoriaView.as_view(), name='detalhe_categoria'),
    path('register/', register, name='register'),
]