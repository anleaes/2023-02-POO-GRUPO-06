from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'alimentos'

router = routers.DefaultRouter()
router.register('', views.AlimentoViewSet, basename='alimentos')

urlpatterns = [
    path('', include(router.urls) )
]