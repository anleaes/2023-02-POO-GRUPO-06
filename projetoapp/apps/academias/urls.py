from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'academias'

router = routers.DefaultRouter()
router.register('', views.AcademiaViewSet, basename='academia')

urlpatterns = [
    path('', include(router.urls) )
]