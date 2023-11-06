# URL
from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, redirect
from django.http import Http404
from .pagination import paginacion
from .models import Proveedor
from .forms import ProveedorForm
from django.views import generic




# Create your views here.
class provListView(generic.ListView):
    template_name = '../templates/suppliers/proveedores.html'
    context_object_name = 'proveedor'
    def get_queryset(self):
        return Proveedor.objects.all()

class provCreateView(generic.CreateView):
    template_name = '../templates/suppliers/createproveedor.html'
    form_class = ProveedorForm

    def get_success_url(self):
        return reverse('suppliers:index')
    
    def get_queryset(self):
        return Proveedor.objects.all()

class provUpdateView(generic.UpdateView):
    template_name = '../templates/suppliers/updateproveedor.html'
    form_class = ProveedorForm

    def get_success_url(self):
        return reverse ('suppliers:index')
    
    def get_queryset(self):
        return Proveedor.objects.all()
    
class provDeleteView(generic.DeleteView):
    template_name = '../templates/suppliers/deleteproveedor.html'
    def get_success_url(self):
        return reverse('suppliers:index')
    
    def get_queryset(self):
        return Proveedor.objects.all()