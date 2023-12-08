from django.db import models

# Create your models here.

class Treinador(models.Model):
    nome = models.CharField('Nome', max_length=50)
    registro = models.TextField('Registro', max_length=100)
    especialidade = models.TextField('Especialidade', max_length=100)
    email = models.TextField('Email', max_length=100)

    class Meta:
        verbose_name = 'Treinador'
        verbose_name_plural = 'Treinadores'
        ordering =['id']
        

    def __str__(self):
        return self.nome
