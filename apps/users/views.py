from django.shortcuts import render, reverse, redirect
from django.http import Http404
from .models import User
from .forms import UserForm
from django.views import generic

class userListView(generic.ListView):
    template_name = 'users/users.html'
    context_object_name = 'usuario'
    def get_queryset(self):
        return User.objects.all()

class userCreateView(generic.CreateView):
    template_name = 'users/createuser.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('suppliers:index')
    
    def get_queryset(self):
        return User.objects.all()

class userUpdateView(generic.UpdateView):
    template_name = 'users/updateuser.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse ('suppliers:index')
    
    def get_queryset(self):
        return User.objects.all()
    
class userDeleteView(generic.DeleteView):
    template_name = 'users/deleteuser.html' 
    def get_success_url(self):
        return reverse('suppliers:index')
    
    def get_queryset(self):
        return User.objects.all()
    
#-- Mostrar el perfil de cada usuario