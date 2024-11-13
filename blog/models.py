from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(
        Category, 
        related_name='posts', 
        blank=True
    )

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-data_postagem']

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.titulo}"

    class Meta:
        ordering = ['-data_postagem']