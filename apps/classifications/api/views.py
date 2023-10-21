# URL
from django.shortcuts import render

# API
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# SERIALIZER
from .serializer import ClasificacionSerializer, UsoTerapeuticoSerializer, FormaAdministracionSerializer

# MODELS
from apps.classifications.models import Clasificacion, UsoTerapeutico, FormaAdministracion
from django.db.models import Q

# Filtro
from .filters import MedicineIdFiltro

# Create your views here.
class UsoTerapeuticoViewSet(viewsets.ModelViewSet):
    queryset = UsoTerapeutico.objects.all()
    serializer_class = UsoTerapeuticoSerializer


class FormaAdministracionViewSet(viewsets.ModelViewSet):
    queryset = FormaAdministracion.objects.all()
    serializer_class = FormaAdministracionSerializer


class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    filter_class = MedicineIdFiltro
