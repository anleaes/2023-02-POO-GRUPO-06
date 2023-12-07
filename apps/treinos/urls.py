from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treinos'

router = routers.DefaultRouter()
router.register('', views.TreinosViewSet, basename='treinos')

urlpatterns = [
    path('', include(router.urls) )
]