from django.db import models
from treinos.models import models
from treinadores.models import Treinador
from clientes.models import Cliente
from exercicios.models import Exercicio

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
