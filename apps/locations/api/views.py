# URL
from django.shortcuts import render
from django.http import Http404

# API
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

# SERIALIZERS
from .serializer import SeccionSerializer, UbicacionSerializer, HistorialInvetarioSerializer

# MODELS
from apps.locations.models import Seccion, Ubicacion, HistorialInvetario

# Create your views here.

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    #permission_classes = [permissions.IsAuthenticated]

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    #permission_classes = [permissions.IsAuthenticated]

class HistorialInventarioViewSet(viewsets.ModelViewSet):
    queryset = HistorialInvetario.objects.all()
    serializer_class = HistorialInvetarioSerializer
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]


# GET - POST
class HistorialInvetarioList(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        locations = HistorialInvetario.objects.all()
        serializer = HistorialInvetarioSerializer(locations, many=True) 
        return Response(serializer.data)
    
    def post(self, request,format=None):        
        serializer = HistorialInvetarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# GET - PUT - DELETE
class HistorialInvetarioDetail(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return HistorialInvetario.objects.get(pk=pk)
        except HistorialInvetario.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None):
        inventario = self.get_object(pk)
        serializer = HistorialInvetarioSerializer(inventario)
        return Response(serializer.data)
    
    def put(self, request,pk,format=None):
        if self.request.user.is_superuser:
            inventario = self.get_object(pk)
            serializer = HistorialInvetarioSerializer(inventario,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        raise Http404
    
    def delete(self, request,pk,format=None):
        if self.request.user.is_superuser:
            inventario = self.get_object(pk)
            inventario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404


