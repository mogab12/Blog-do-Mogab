from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

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