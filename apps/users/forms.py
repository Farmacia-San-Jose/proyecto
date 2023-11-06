from django import forms
from .models import User
from django.forms import *

class UserForm(ModelForm): 
    class Meta: 
        model = User 
        fields = '__all__'
        widgets = {
            'first_name':TextInput(attrs = {'type': 'text'}),
            'last_name': TextInput(attrs={'type':'text'}),
            'username': TextInput(attrs={'type': 'text'}),
            'telephone': NumberInput(attrs={'type': 'number'}),
        }