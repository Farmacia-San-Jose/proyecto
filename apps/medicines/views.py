# URL
from django.shortcuts import render, redirect, get_object_or_404

# CODIGOS HTTP
from django.http import Http404
from django.http import HttpResponse

# DJANGO
from django.shortcuts import render
from django.db import transaction

# CONSULTA
from .consultas.resultado_consulta import listar, existencia, vencidos


# MODEL
from apps.medicines.models import Medicamento as MedicamentoModel, HistorialMedicamento as HistorialMedicamentoModel
from apps.locations.models import HistorialInvetario, Ubicacion
from apps.classifications.models import Clasificacion, UsoTerapeutico, FormaAdministracion
from apps.suppliers.models import Proveedor
from apps.presentations.models import Presentacion
from django.db.models import Q

# PAGINACION
from .pagination import paginacion

# CLASES
from apps.medicines.clases.medicamentos import Medicamento
from apps.medicines.clases.medicamentos import listar_medicamento, listar_historial_medicamento

import json
import itertools

from datetime import datetime, date

fecha_actual = datetime.now()
fecha_actual_solo_fecha = fecha_actual.date()


# Create your views here.
def index(request):
    
    # OBTENER MEDICAMENTOS
    listar_medicamento()

    medicine_list = MedicamentoModel.objects.all()
    # OBTENER UBICACIONES
    ubicacion_list = Ubicacion.objects.all()
    
    #OBTENER LA CLASIFICACION
    clasificacion_list = Clasificacion.objects.all()

    # OBTENER EL HISTORIAL DEL MEDICAMENTO
    historial_medico_list = listar_historial_medicamento()

    # OBTENER EL HISTORIAL DE INVENTARIO
    historial_inventario_list = HistorialInvetario.objects.all()
    
    
    # PAGINACION
    
    page_obj = paginacion(request,medicine_list)

    # TEMPLATE
    template_name = 'medicines/index.html' 

   
    
    contador = 0


    # CONEXTO
    context = {
        'title':'Medicamentos',
        'page_obj':page_obj,
        'medicamento_list':medicine_list,
        'ubicacion_list':ubicacion_list,
        'clasificacion_list':clasificacion_list,
        'historial_medico_list':historial_medico_list,
        'historial_inventario_list':historial_inventario_list,
        
    }
    
    return render(request,template_name, context)






def add(request):
    context = {

        'title':'Registro de Medicamento'
    }

    if request.method == 'POST':

        with transaction.atomic():

            # Atributos para el apartado de medicina
            medicina_name = request.POST.get('medicine_name')
            medicine_description = request.POST.get('medicine_description')

            # Guardar informacion
            medicina = MedicamentoModel(medicine_name=medicina_name, description=medicine_description)
            medicina.save()

            medicina_id = get_object_or_404(MedicamentoModel, id = medicina.id)
            
            
            # Segun su clasificacion
            clasificacion = Clasificacion()
            clasificacion.medicine_id = medicina_id
            opciones_uso = request.POST.getlist('opciones_uso[]')
            opciones_forma = request.POST.getlist('opciones_forma[]')
            
            combinar = itertools.zip_longest(opciones_uso, opciones_forma, fillvalue=None)

            for uso, forma in combinar:
                if uso != None:
                    uso_id = get_object_or_404(UsoTerapeutico, id = uso)
                    clasificacion.therepeuticuse_id = uso_id

                if forma !=None:
                    forma_id = get_object_or_404(FormaAdministracion, id = forma)                
                    clasificacion.formadministration_id = forma_id
                
                clasificacion.save()


            # Historial de medicamento

            historialM = HistorialMedicamentoModel()
            historialM.medicine_id = medicina_id

            presentacion = request.POST.get('tipo_presentacion')
            if presentacion != None:
                presentacion_id = get_object_or_404(Presentacion, id=presentacion)
                historialM.presentation_id = presentacion_id

            proveedor = request.POST.get('proveedor_select')

            if proveedor != None:
                proveedor_id = get_object_or_404(Proveedor, id = proveedor )
                historialM.supplier_id = proveedor_id

            cost_price = request.POST.get('cost_price')
            marca = request.POST.get('brand')
            fecha_vencimiento = request.POST.get('fecha_vencimiento')
            codigo = request.POST.get('code_medicine')
            
            
            
            historialM.cost_price = cost_price
            historialM.brand = marca
            historialM.medication_code = codigo
            historialM.expiration_date = fecha_vencimiento
            historialM.save()

            # Historial de inventario 
            historialI = HistorialInvetario()
            historialI.medicine_id= medicina_id
            cantidad = request.POST.get('cantidad')    
            sale_price = request.POST.get('sale_price')

            historialI.quantity_stock = cantidad
            historialI.sale_price = sale_price
            historialI.save() 

            return redirect('medicines:index')



    return render(request, 'medicines/base/form.html', context)
    
    