# URL
from django.shortcuts import render

# CODIGOS HTTP
from django.http import Http404

# API
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# SERIALIZERS
from .serializer import MedicamentoSerializer, HistorialMedicamentorSerializer

# MODEL
from apps.medicines.models import Medicamento, HistorialMedicamento

# Create your views here.
class MedicamentoViewSet(viewsets.ModelViewSet):    
    serializer_class = MedicamentoSerializer
    queryset = Medicamento.objects.all()
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

class HistorialMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedicamento.objects.all()
    serializer_class = HistorialMedicamentorSerializer
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]


# ------------------------- MEDICAMENTO -----------------------------
class MedicamentoList(APIView):
    # GET Y POST
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        medicine = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicine, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicamentoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Medicamento.objects.get(pk=pk)
        except Medicamento.DoesNotExist:
            raise Http404
        
    def get(self,request, pk,format=None):
        medicine = self.get_object(pk)
        serializer = MedicamentoSerializer(medicine)
        return Response(serializer.data)
    
    def put(self, request, pk,format=None):
        if self.request.user.is_superuser:
            medicine = self.get_object(pk)
            serializer = MedicamentoSerializer(medicine,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        raise Http404
    
    def delete(self, request, pk, format=None):
        if self.request.user.is_superuser:
            medicine = self.get_object(pk)
            medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404
    
#-------------- HISTORIAL MEDICAMENTO ----------------------
class HistorialMedicamentoList(APIView):
    # GET Y POST
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        medicine = HistorialMedicamento.objects.all()
        serializer = HistorialMedicamentorSerializer(medicine, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistorialMedicamentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistorialMedicamentoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return HistorialMedicamento.objects.get(pk=pk)
        except HistorialMedicamento.DoesNotExist:
            raise Http404
        
    def get(self,request, pk,format=None):
        medicine = self.get_object(pk)
        serializer = HistorialMedicamentorSerializer(medicine)
        return Response(serializer.data)
    
    def put(self, request, pk,format=None):
        if self.request.user.is_superuser:
            medicine = self.get_object(pk)
            serializer = HistorialMedicamentorSerializer(medicine,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        raise Http404
    
    def delete(self, request, pk, format=None):
        if self.request.user.is_superuser:
            medicine = self.get_object(pk)
            medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404