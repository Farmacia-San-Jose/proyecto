# URL
from django.shortcuts import render
from django.http import Http404

# API
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

# SERIALIZER
from .serializer import PresentacionSerializer

# MODELS
from apps.presentations.models import Presentacion

# Create your views here.
class PresentacionviewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

# GET - POST
class PresentacionList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request,format=None):
        presentation = Presentacion.objects.all()
        serializer = PresentacionSerializer(presentation,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PresentacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET - PUT -DELETE
class PresentacionDetail(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Presentacion.objects.get(pk=pk)
        except Presentacion.DoesNotExist:
            raise Http404
        
    def get(self,request,pk, format=None):
        presentation = self.get_object(pk)
        serializer = PresentacionSerializer(presentation)
        return Response(serializer.data)
        

    def put(self,request,pk, format=None):
        if self.request.user.is_superuser:
            presentation = self.get_object(pk)
            serializer = PresentacionSerializer(presentation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404
    
    def delete(self,request,pk, format=None):
        if self.request.user.is_superuser:
            presentation = self.get_object(pk)
            presentation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404