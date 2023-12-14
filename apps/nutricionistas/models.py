from django.db import models
from academias.models import Academia

# Create your models here.

class Nutricionista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    registro = models.CharField(max_length=14, unique=True)
    especialidade = models.TextField('especialidade', max_length=100)
    email = models.TextField('email', max_length=100)
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'nutricionista'
        verbose_name_plural = 'Nutricionistas'
        ordering =['id']

    def __str__(self):
        return self.nome
