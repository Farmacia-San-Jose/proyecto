# API

from rest_framework import serializers

# MODELS
from apps.suppliers.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'