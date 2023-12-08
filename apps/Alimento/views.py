from django.shortcuts import render

# Create your views here.

from .models import Alimento
from rest_framework import viewsets
from .serializer import AlimentoSerializer


class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer