from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treinadores'

router = routers.DefaultRouter()
router.register('', views.TreinadorViewSet, basename='treinadores')

urlpatterns = [
    path('', include(router.urls) )
]