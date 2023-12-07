from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Alimento'

router = routers.DefaultRouter()
router.register('', views.AlimentoViewSet, basename='Alimento')

urlpatterns = [
    path('', include(router.urls) )
]