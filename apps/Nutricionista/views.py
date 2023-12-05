from django.shortcuts import render
from .models import Nutricionista
from rest_framework import viewsets
from .serializer import NutricionistaSerializer

# Create your views here." 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Nutricionista.objects.all()
    serializer_class = NutricionistaSerializer 