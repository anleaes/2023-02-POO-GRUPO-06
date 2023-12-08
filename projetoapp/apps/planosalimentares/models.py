from django.db import models
from Cliente.models import Cliente
from Nutricionista.models import Nutricionista  
from Alimento.models import Alimento

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