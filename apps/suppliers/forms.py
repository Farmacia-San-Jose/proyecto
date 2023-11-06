from django import forms
from .models import Proveedor
from django.forms import *

class ProveedorForm(ModelForm): 
    class Meta: 
        model = Proveedor 
        fields = '__all__'
        widgets = {
            'first_name':TextInput(attrs = {'type': 'text'}),
            'last_name': TextInput(attrs={'type':'text'}),
            'company': TextInput(attrs={'type': 'text'}),
            'telephone': NumberInput(attrs={'type': 'number'}),
            'correo': EmailField(max_length = 200)
        }