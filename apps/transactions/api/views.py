# URL
from django.shortcuts import render
from django.http import Http404

# API
from rest_framework import viewsets,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response


# SERIALIZER
from apps.transactions.api.serializer import HistorialTransaccionSerializer, DetalleTransaccionSerializer

# MODELS
from apps.transactions.models import HistorialTransaccion, DetalleTransaccion

# Create your views here.
class HistorialTransaccionViewSet(viewsets.ModelViewSet):
    queryset = HistorialTransaccion.objects.all()
    serializer_class = HistorialTransaccionSerializer
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

class DetalleTransaccionViewSet(viewsets.ModelViewSet):
    queryset = DetalleTransaccion.objects.all()
    serializer_class = DetalleTransaccionSerializer
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

# ----------------- TRANSACTION ---------------------

# GET-POST
class HistorialTransaccionList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        transaction = HistorialTransaccion.objects.all()
        serializer = HistorialTransaccionSerializer(transaction, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HistorialTransaccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.data()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET - PUT - DELETE
class HistorialTransaccionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return HistorialTransaccion.objects.get(pk=pk)
        except HistorialTransaccion.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        transaction = self.get_object(pk)
        serializer = HistorialTransaccionSerializer(transaction)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        if self.request.user.is_superuser:
            transaction = self.get_object(pk)
            serializer = HistorialTransaccionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404
    
    def delete(self, request, pk, format=None):
        if self.request.user.is_superuser:
            transaction = self.get_object(pk)
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404

# ------------------- DETAIL TRANSACTION -----------
# GET-POST
class DetailTransaccionList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        transaction = DetalleTransaccion.objects.all()
        serializer = DetalleTransaccionSerializer(transaction, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DetalleTransaccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.data()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET - PUT - DELETE
class DetailTransaccionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return DetalleTransaccion.objects.get(pk=pk)
        except DetalleTransaccion.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        transaction = self.get_object(pk)
        serializer = DetalleTransaccionSerializer(transaction)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        if self.request.user.is_superuser:
            transaction = self.get_object(pk)
            serializer = DetalleTransaccionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404
    
    def delete(self, request, pk, format=None):
        if self.request.user.is_superuser:
            transaction = self.get_object(pk)
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404