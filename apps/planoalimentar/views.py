from django.shortcuts import render
from .models import Planoalimentar
from rest_framework import viewsets
from .serializer import PlanoalimentarSerializer

# Create your views here.

class PlanoalimentarViewSet(viewsets.ModelViewSet):
    queryset = Planoalimentar.objects.all()
    serializer_class = PlanoalimentarSerializer  