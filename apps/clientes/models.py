from django.db import models
from academias.models import Academia

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    genero = models.CharField(max_length=14, unique=True)
    peso = models.FloatField()
    altura = models.FloatField()
    dataNascimento = models.CharField(max_length=10, unique=True)
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome