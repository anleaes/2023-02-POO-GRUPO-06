from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'nutricionistas'

router = routers.DefaultRouter()
router.register('', views.NutricionistaViewSet, basename='nutricionistas')

urlpatterns = [
    path('', include(router.urls) )
]