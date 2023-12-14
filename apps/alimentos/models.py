from django.db import models

# Create your models here.
class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    kcal = models.CharField(max_length=14, unique=True)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering =['id']

    def __str__(self):
        return self.nome