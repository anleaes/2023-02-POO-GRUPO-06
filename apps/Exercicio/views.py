from django.shortcuts import render

# Create your views here.

from .models import Exercicio
from rest_framework import viewsets
from .serializer import ExercicioSerializer

# Após o comentario "# Create your views here." e crie as views "Pessoa".

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer