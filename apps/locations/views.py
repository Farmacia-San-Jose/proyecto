# URL
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# MODELS
from .models import Seccion, Ubicacion, HistorialInvetario
from apps.medicines.models import HistorialMedicamento, Medicamento

# Create your views here.

# LISTAR SEGUN EL TIPO DE UBICACION
def list_locations(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    cantidad_elementos = HistorialInvetario.objects.all().filter(location_id=ubicacion).count()
    ubicacion_list = Ubicacion.objects.all()
    medicine_list = HistorialInvetario.objects.all().filter(location_id=ubicacion)
    

    context = {
        'title':'Medicamentos por ubicacion: {}'.format(ubicacion),
        'ubicacion':ubicacion,
        'cantidad':cantidad_elementos,
        'ubicacion_list':ubicacion_list,
        'medicamento_list':medicine_list,
    }

    return render(request, 'locations/index.html', context)