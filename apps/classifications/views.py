# URL
from django.shortcuts import render, redirect, get_object_or_404


# MODELS
from .models import Clasificacion, UsoTerapeutico, FormaAdministracion

#DJANGO
from django.contrib.auth.decorators import login_required

@login_required
def agregar_uso(request):
    if request.method == 'POST':
        print('PROCESANDOOOO')
        tipo_uso = request.POST.get('tipo_uso_terapeutico')
        descripcion = request.POST.get('description_uso')
        uso = UsoTerapeutico()
        uso.type_therepeuticuse = tipo_uso
        uso.description = descripcion
        uso.save()
        dire = request.POST.get('redireccionar')
        redirect('index')
    
    context ={
        'title':'Agregar Uso Terapeutico Modal'
    }
    
    return render(request, 'medicines/modal/modalUsoTerapeutico.html',context)