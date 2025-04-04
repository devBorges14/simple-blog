from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    image = models.ImageField(upload_to='images/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_publicacao']  # Ordenação padrão: mais antigos primeiro

    def __str__(self):
        return self.titulo
