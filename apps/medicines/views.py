# URL
from django.shortcuts import render, redirect, get_object_or_404

# CODIGOS HTTP
from django.http import Http404
from django.http import HttpResponse

# DJANGO
from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.decorators import login_required

# CONSULTA
from .consultas.resultado_consulta import listar, existencia, vencidos


# MODEL
from apps.medicines.models import Medicamento as MedicamentoModel, HistorialMedicamento as HistorialMedicamentoModel
from apps.locations.models import HistorialInvetario, Ubicacion, Seccion
from apps.classifications.models import Clasificacion, UsoTerapeutico, FormaAdministracion
from apps.suppliers.models import Proveedor
from apps.presentations.models import Presentacion
from django.db.models import Q

# PAGINACION
from .pagination import paginacion

# CLASES
from apps.medicines.clases.medicamentos import listar_medicamento, listar_historial_medicamento

import json
import itertools

from datetime import datetime, date

fecha_actual = datetime.now()
fecha_actual_solo_fecha = fecha_actual.date()



#------- Funcion para guardar informacion
def guardar(request):
     # Atributos para el apartado de medicina
    medicina_name = request.POST.get('medicine_name')
    medicine_description = request.POST.get('medicine_description')

    # Guardar informacion
    medicina = MedicamentoModel(medicine_name=medicina_name, description=medicine_description)
    medicina.save()

    medicina_id = get_object_or_404(MedicamentoModel, id = medicina.id)
            
            
    # Segun su clasificacion
    with transaction.atomic():
        
        opciones_uso = request.POST.getlist('opciones_uso[]')
        opciones_forma = request.POST.getlist('opciones_forma[]')
                
        combinar = itertools.zip_longest(opciones_uso, opciones_forma, fillvalue=None)

        for uso, forma in combinar:
            clasificacion = Clasificacion()
            clasificacion.medicine_id = medicina_id
            if uso != None:
                uso_id = get_object_or_404(UsoTerapeutico, id = uso)
                tener_uso = uso_id

            if forma !=None:
                forma_id = get_object_or_404(FormaAdministracion, id = forma)                
                tener_forma= forma_id
                    
                
            clasificacion.therepeuticuse_id = tener_uso
            clasificacion.formadministration_id = tener_forma
            #print(f' USO TERAPEUTICO - {clasificacion.therepeuticuse_id}')
            #print(f'FORMA DE ADMINISTRACION - {clasificacion.formadministration_id}')
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
    ubic = request.POST.get('ubicacion')
    if ubic != None:
        historialI.location_id = get_object_or_404(Ubicacion, id= ubic)
    
    sec = request.POST.get('seccion')
    if sec !=None:
        historialI.locationsection_id = get_object_or_404(Seccion, id=sec)
    historialI.row = request.POST.get('fila')
    historialI.column = request.POST.get('column')
    historialI.save()



# Create your views here.
#------- LISTAR TODOS LOS MEDICAMENTOS REGISTRADOS
@login_required
def index(request):
    
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


# ---- REGISTRAR UN MEDICAMENTO
@login_required
def add(request):
    
    context = {

        'title':'Registro de Medicamento'
    }

    if request.method == 'POST':
        resultado = request.POST.get('resultado')
        if resultado == 'true':
            guardar(request)
            return redirect('medicines:index')
        elif resultado == 'false':
            return redirect('medicines:agregar')



    return render(request, 'medicines/base/form.html', context)
    

# ------------- MODULO DE ACTULIZAR ---------------------
@login_required
def update(request, id):
    if not request.user.is_superuser:
        return redirect('medicines:index')
    
    medicina = get_object_or_404(MedicamentoModel, id=id)
    proveedores = Proveedor.objects.all()
    historial_mediamento_list = HistorialMedicamentoModel.objects.all().filter(medicine_id=medicina)
    presentacion_list = Presentacion.objects.all()

    combinar = itertools.zip_longest(proveedores, historial_mediamento_list, fillvalue=None)
    combinar2 = itertools.zip_longest(presentacion_list, historial_mediamento_list, fillvalue=None)
    
    
    if request.method == 'POST':
        resultado = request.POST.get('resultado')
        if resultado == 'true':
            print('Ejecutar el programa')
            medicina.medicine_name = request.POST['medicine_name']
            medicina.description = request.POST['medicine_description']
            medicina.save()
        
            clasificacion = Clasificacion.objects.all().filter(medicine_id=medicina)
            opciones_uso = request.POST.getlist('opciones_uso[]')
            opciones_forma = request.POST.getlist('opciones_forma[]')
            combinacion_clasificacion = list(itertools.zip_longest(opciones_uso, opciones_forma,fillvalue=None))
            temp_seleccionados =[]
            for uso, forma in combinacion_clasificacion:
                temp_temp =[]
                if (uso != None):
                    uso_id = get_object_or_404(UsoTerapeutico, id = uso)

                if(forma !=None):
                    forma_id = get_object_or_404(FormaAdministracion, id = forma)
                

                temp_temp.append(uso_id)
                temp_temp.append(forma_id)

                temp_seleccionados.append(temp_temp)

            

            ver_seleccionados = list(itertools.zip_longest(temp_seleccionados, clasificacion, fillvalue=None))
            if ( len(temp_seleccionados) == len(clasificacion) ):
                print('Se siguen manteniendo la cantidad de seleccionados')
                print('Pasar a verificar cada valor')
                for select, clasi in ver_seleccionados:
                    clasi.therepeuticuse_id = select[0]
                    clasi.formadministration_id = select[1]
                    clasi.save()
                
            elif( len(temp_seleccionados) <= len(clasificacion)):
                print('Se ha quitado mas de algun dato seleccionado')
                print('Revisar!!!')
                for select, clasi in ver_seleccionados:
                    if select != None:
                        clasi.therepeuticuse_id = select[0]
                        clasi.formadministration_id = select[1]
                        clasi.save()
                    else:
                        clasi.delete()
            else:
                print('Se ha agregado un nuevo valor')
                #-- clasificar 
                for select, clasi in ver_seleccionados:
                    if clasi == None:
                        clasifi = Clasificacion()
                        clasifi.medicine_id = medicina
                        clasifi.therepeuticuse_id = select[0]
                        clasifi.formadministration_id = select[1]
                        clasifi.save()
            
            
            
            histo_medico = HistorialMedicamentoModel.objects.all().filter(medicine_id=medicina)
            for hm in histo_medico:
                hm.supplier_id = get_object_or_404(Proveedor, id = request.POST.get('proveedor_select'))
                hm.presentation_id = get_object_or_404(Presentacion, id = request.POST.get('tipo_presentacion'))
                hm.brand = request.POST.get('brand')
                hm.cost_price = request.POST.get('cost_price')
                hm.medication_code = request.POST.get('code_medicine')
                hm.expiration_date = request.POST.get('fecha_vencimiento')
                hm.save()
            
            histo_inventario = HistorialInvetario.objects.all().filter(medicine_id=medicina)
            for hi in histo_inventario:
                hi.quantity_stock = request.POST.get('cantidad')
                hi.sale_price = request.POST.get('sale_price')
                ubica = request.POST.get('ubicacion')
                if ubica != None:
                    hi.location_id = get_object_or_404(Ubicacion,id= ubica)
                
                secc = request.POST.get('seccion')
                if secc != None:
                    hi.locationsection_id = get_object_or_404(Seccion, id=secc)
                
                hi.row = request.POST.get('fila')
                hi.column = request.POST.get('column')

                hi.save()
            return redirect('medicines:index')
            
        elif(resultado == 'false'):
            print('Volviendo a ingresar datos')
            return redirect('medicines:actualizar',str(id))
    
    context = {
            'title':'Actualizando {}'.format(medicina),
            'medicine':medicina,
            'combinacion_list':combinar,
            'combinacion_list_2':combinar2,
            'historial_mediamento_list':historial_mediamento_list,     
    }
    return render(request, 'medicines/base/update_form.html', context)


#---------- Modulo para eliminar --------- 
@login_required
def delete(request, id):
    if not request.user.is_superuser:
        return redirect('medicines:index')
    medicine_id = get_object_or_404(MedicamentoModel, id=id)
    medicine_id.delete()


#---------- Modulo de detalle --------------
@login_required
def detail(request, id):
    medicine_id = get_object_or_404(MedicamentoModel, id=id)
    historial_inventario = HistorialInvetario.objects.all().filter(medicine_id=medicine_id)
    historial_medicamento = HistorialMedicamentoModel.objects.all().filter(medicine_id=medicine_id)
    clasificacion = Clasificacion.objects.all().filter(medicine_id=medicine_id)
    context = {
        'title': '{}'.format(medicine_id),
        'medicine':medicine_id,
        'historial_inventario':historial_inventario,
        'historial_medicamento':historial_medicamento,
        'clasificacion':clasificacion
    }
    return render(request, 'medicines/detail.html', context)