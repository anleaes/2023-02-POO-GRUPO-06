from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'planosalimentares'

router = routers.DefaultRouter()
router.register('', views.PlanoalimentarViewSet, basename='planosalimentares')

urlpatterns = [
    path('', include(router.urls) )
]

