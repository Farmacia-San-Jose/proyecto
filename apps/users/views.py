from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import User
from .forms import UserForm, UpdateUserForm, RegistroForm
from django.views import generic
from django.urls import reverse_lazy, reverse

#Decorador
from django.contrib.auth.decorators import login_required

class userListView(generic.ListView):
    template_name = 'users/users.html'
    context_object_name = 'usuario'
    def get_queryset(self):
        return User.objects.all()
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        return context

class userCreateView(generic.CreateView):
    template_name = 'users/createuser.html'
    form_class = RegistroForm
    model = User

    success_url = reverse_lazy(('users:index'))

    
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Nuevo Usuario'
        return context
    
    

class userUpdateView(generic.UpdateView):
    template_name = 'users/updateuser.html'
    form_class = UpdateUserForm
    model = User

    success_url = reverse_lazy(('users:index'))
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Usuario'
        return context
    
    
    
class userDeleteView(generic.DeleteView):
    template_name = 'users/deleteuser.html' 
    success_url = reverse_lazy(('users:index'))
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Usuario'
        return context
    
    def get_queryset(self):
        return User.objects.all()
    
#-- Mostrar el perfil de cada usuario}
@login_required
def perfil(request):
    user = get_object_or_404(User, id=request.user.id)
    
    context = {
        'title':'{}'.format(request.user),
        'user':user
    }
    return render(request, 'users/perfil.html',context)
