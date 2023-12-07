from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']