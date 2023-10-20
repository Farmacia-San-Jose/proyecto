# API
from rest_framework import serializers

# MODELS
from apps.presentations.models import Presentacion

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = '__all__'

        