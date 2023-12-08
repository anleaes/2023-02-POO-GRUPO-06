from .models import Academia
from rest_framework import serializers

class AcademiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academia
        fields = '__all__'