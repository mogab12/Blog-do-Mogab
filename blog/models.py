from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detalhe', kwargs={'pk': self.pk})

    # Adicione esta linha para ordenação padrão
    class Meta:
        ordering = ['-data_postagem']