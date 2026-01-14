from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=200)
    link = models.URLField()
    conteudo = models.TextField()
    confiavel = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
