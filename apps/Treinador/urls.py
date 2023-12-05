from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Treinador'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='Treinador')

urlpatterns = [
    path('', include(router.urls) )
]