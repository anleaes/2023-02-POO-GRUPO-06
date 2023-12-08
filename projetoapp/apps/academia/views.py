from django.shortcuts import render
from .models import Academia
from rest_framework import viewsets
from .serializer import AcademiaSerializer

# Create your views here." 

class AcademiaViewSet(viewsets.ModelViewSet):
    queryset = Academia.objects.all()
    serializer_class = AcademiaSerializer 