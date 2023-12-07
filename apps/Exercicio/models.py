from django.db import models

# Create your models here.

class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.IntegerField()
    Maquina = models.IntegerField()
    grupoMuscular = models.IntegerField()

    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering =['id']

    def __str__(self):
        return self.nome