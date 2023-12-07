from django.shortcuts import render

# Create your views here.

from .models import Cliente
from rest_framework import viewsets
from .serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer