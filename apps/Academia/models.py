from django.db import models

# Create your models here.

class Academia(models.Model):
    endereço = models.CharField('Endereço', max_length=50)
    horarioFuncionamento = models.TextField('Descricao', max_length=100)
    telefone = models.CharField('Telefone',max_length=14, unique=True)
    
    class Meta:
        verbose_name = 'Academia'
        verbose_name_plural = 'Academia'
        ordering =['id']

    def __str__(self):
        return self.endereço
