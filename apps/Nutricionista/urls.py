from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Nutricionista'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='Nutricionista')

urlpatterns = [
    path('', include(router.urls) )
]