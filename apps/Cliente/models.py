from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=14, unique=True
    genero = models.IntegerField()
    peso = models.CharField(max_length=14, unique=True
    altura = models.CharField(max_length=14, unique=True
    dataNascimento = models.CharField(max_length=14, unique=True
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome