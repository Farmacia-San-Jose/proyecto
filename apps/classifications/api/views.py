# URL
from django.shortcuts import render

# API
from rest_framework import viewsets, permissions

# SERIALIZER
from .serializer import ClasificacionSerializer, UsoTerapeuticoSerializer, FormaAdministracionSerializer

# MODELS
from apps.classifications.models import Clasificacion, UsoTerapeutico, FormaAdministracion


# Create your views here.
class UsoTerapeuticoViewSet(viewsets.ModelViewSet):
    queryset = UsoTerapeutico.objects.all()
    serializer_class = UsoTerapeuticoSerializer
    permission_classes = [permissions.IsAuthenticated]

class FormaAdministracionViewSet(viewsets.ModelViewSet):
    queryset = FormaAdministracion.objects.all()
    serializer_class = FormaAdministracionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    permission_classes = [permissions.IsAuthenticated]