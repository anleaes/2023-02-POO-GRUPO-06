from django.shortcuts import render
from .models import Treinos
from rest_framework import viewsets
from .serializer import TreinosSerializer

# Create your views here.
class TreinosViewSet(viewsets.ModelViewSet):
    queryset = Treinos.objects.all()
    serializer_class = TreinosSerializer  
    