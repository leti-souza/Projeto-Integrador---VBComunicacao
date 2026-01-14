from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_CHOICES = (
        ('jornalista', 'Jornalista'),
        ('coordenador', 'Coordenador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"
