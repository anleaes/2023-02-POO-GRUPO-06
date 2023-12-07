from django.db import models
from clients.models import Client
from Treinador.models import Treinador
#from exercicio.models import Exercicio

# Create your models here.
class Treinos(models.Model):
    series = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    repeticoes = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    descanso = models.TextField('Descanso', max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    #exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'
      

    def __str__(self):
        return self.name