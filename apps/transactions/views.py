# URL
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

# MODELS
from .models import HistorialTransaccion, DetalleTransaccion

# FORMULARIO
from .forms import HistorialTransaccionForm

# LISTADO DE INFORMACION UNIDA
from apps.medicines.consultas.unir_datos import informacion_completa_medicamento
# Create your views here.

@login_required
def agregar_transaccion(request):
    
    context = {
        'title':'Realizar Transaccion',
        'form':HistorialTransaccionForm,
        'user':request.user,
        'medicines': informacion_completa_medicamento(),
    }
    return render(request, 'transactions/forms/add.html', context)