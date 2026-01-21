from django.contrib.auth.models import User
from django.db import models
#from django.db import models



class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=200)
    link = models.URLField()
    conteudo = models.TextField()
    confiavel = models.BooleanField(null=True)
    visualizacoes = models.PositiveIntegerField(default=0)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='favoritos')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'noticia')

    def __str__(self):
        return f"{self.usuario.username} ⭐ {self.noticia.titulo}"