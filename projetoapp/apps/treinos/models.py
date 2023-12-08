from django.db import models
#from treinos.models import models
from treinador.models import Treinador
from cliente.models import Cliente
from exercicio.models import Exercicio

# Create your models here.
class Treino(models.Model):
    serie = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    repeticao = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    descanso = models.TextField('Descanso', max_length=100)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    treinador = models.ForeignKey('Treinador', on_delete=models.CASCADE)
    exercicio = models.ForeignKey('Exercicio', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'
      

    def __str__(self):
        return self.serie