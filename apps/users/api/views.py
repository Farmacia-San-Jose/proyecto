# URL
# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

# API
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# SERIALIZER
from .serializers import UserSerializer

# MODELOS
from apps.users.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]


# GET - POST
class UserList(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        
        if self.request.user.is_superuser:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404

# GET - PUT - DELETE
class UserDetail(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)
            
    
    def put(self, request, pk, format=None):
        if self.request.user.is_superuser:
            users = self.get_object(pk)
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise Http404
    
    def delete(self, request, pk, format=None):
        if self.request.user.is_superuser:
            users = self.get_object(pk)
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise Http404