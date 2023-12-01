from .models import Academia
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academia
        fields = '__all__'