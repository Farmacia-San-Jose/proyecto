# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import Http404

# Login
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

### -- APARTADO DE INICIO DE SESION --##
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')  # diccionario
        password = request.POST.get('password')  # None

        user = authenticate(username=username, password=password)  # None
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            if user.is_superuser:
                messages.success(
                    request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))

            else:
                messages.success(
                    request, 'Bienvenido USUARIO: {}'.format(user.username))

            return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, "users/login.html", {
        'title': 'Iniciar Sesion',

    })

### -- APARTADO DE SALIR --##
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def index(request):
    template = 'index.html'
    context = {
        'title': 'Inicio'
    }   
    return render(request, template, context)