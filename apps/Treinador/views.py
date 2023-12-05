from django.shortcuts import render
from .models import Treinador
from rest_framework import viewsets
from .serializer import TreinadorSerializer

# Create your views here." 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Treinador.objects.all()
    serializer_class = TreinadorSerializer 