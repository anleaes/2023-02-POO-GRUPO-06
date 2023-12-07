from .models import Treinos
from rest_framework import serializers

class TreinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinos
        fields = '__all__'