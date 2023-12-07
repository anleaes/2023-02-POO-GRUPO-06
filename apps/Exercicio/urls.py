from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Exercicio'

router = routers.DefaultRouter()
router.register('', views.ExercicioViewSet, basename='Exercicio')

urlpatterns = [
    path('', include(router.urls) )
]