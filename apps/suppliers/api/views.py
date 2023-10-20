# URL
from django.shortcuts import render
from django.http import Http404

# API
from rest_framework import viewsets,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response

# SERIALIZER
from .serializer import ProveedorSerializer

# MODELS
from apps.suppliers.models import Proveedor

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

# GET- POST
class ProveedorList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        proveedor = Proveedor.objects.all()
        seriealizer = ProveedorSerializer(proveedor, many=True)
        return Response(seriealizer.data)
    
    def post(self, request, format=None):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET - PUT - DELETE
class ProveedorDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        suppliers = self.get_object(pk)
        serializer = ProveedorSerializer(suppliers)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        if self.request.user.is_superuser:
            suppliers = self.get_object(pk)
            serializer = ProveedorSerializer(suppliers,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404
    
    def delete(self, request, pk, format=None):
        if  self.request.user.is_superuser:
            suppliers = self.get_object(pk)
            suppliers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404

