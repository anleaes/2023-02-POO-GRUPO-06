"""modeloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/', include('academias.urls', namespace='academias')),
    path('cliente/', include('clientes.urls', namespace='clientes')),
    path('treino/', include('treinos.urls', namespace='treinos')),
    path('treinador/', include('treinadores.urls', namespace='treinadores')),
    path('exercici/', include('exercicios.urls', namespace='exercicios')),
    path('nutricionista/', include('nutricionistas.urls', namespace='nutricionistas')),
    path('alimento/', include('alimentos.urls', namespace='alimentos')),
    path('planoalimentar/', include('planosalimentares.urls', namespace='planosalimentares')),
]
