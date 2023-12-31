from django.db import models
from clientes.models import Cliente
from exercicios.models import Exercicio
from alimentos.models import Alimento
from nutricionistas.models import Nutricionista

# Create your models here.

class Planoalimentar(models.Model):
    horariosRefeicoes = models.CharField('Nome', max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    alimento  = models.ForeignKey(Alimento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Planoalimentar'
        verbose_name_plural = 'Planosalimentares'
        ordering =['id']
        

    def __str__(self):
        return self.horariosRefeicoes