from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exercicios'

router = routers.DefaultRouter()
router.register('', views.ExercicioViewSet, basename='exercicios')

urlpatterns = [
    path('', include(router.urls) )
]