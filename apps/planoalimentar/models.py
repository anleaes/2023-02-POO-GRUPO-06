from django.db import models
from clients.models import Client
from Nutricionista.models import Nutricionista  
#from Alimentos.models import Alimentos

# Create your models here.
class Planoalimentar(models.Model):
    horariosRefeicoes = models.CharField('Nome', max_length=50)
    
    
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    #Alimentos  = models.ForeignKey(Alimentos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Planoalimentar'
        

    def __str__(self):
        return self.horariosRefeicoes
