from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'planoalimentar'

router = routers.DefaultRouter()
router.register('', views.PlanoalimentarViewSet, basename='Planoalimentar')


urlpatterns = [
    path('', include(router.urls) )
]

