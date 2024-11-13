from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    path('post/criar/', views.criar_post, name='criar_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/remover/', views.remover_post, name='remover_post'),
]