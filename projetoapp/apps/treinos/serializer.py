from .models import Treino
from rest_framework import serializers

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinos
        fields = '__all__'