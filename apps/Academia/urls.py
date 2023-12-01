from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Academia'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='Academia')

urlpatterns = [
    path('', include(router.urls) )
]