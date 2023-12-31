# URL
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required

# MODELS
from .models import HistorialTransaccion, DetalleTransaccion
from apps.medicines.models import Medicamento, HistorialMedicamento
from apps.users.models import User

# FORMULARIO
from .forms import HistorialTransaccionForm

# LISTADO DE INFORMACION UNIDA
from apps.medicines.consultas.unir_datos import informacion_completa_medicamento

# JSON
import json
from django.http import JsonResponse

# MENSAJE 
from django.contrib import messages

#Paginacion
from .pagination import paginacion

# Create your views here.

#Eliminar una transaccion
@login_required
def eliminar(request, id):
    if not request.user.is_superuser:
        return redirect('transactions:index')
    
    historial = get_object_or_404(HistorialTransaccion, id=id)
    historial.delete()
    messages.success(request, 'Se ha eliminado correctamente')
    return redirect('transactions:index')

#--- DETALLE DE CADA TRANSACCION
@login_required
def detalle_transaccion(request, id):
    detalle_transaccions = get_object_or_404(HistorialTransaccion, id=id) 
    detalles_historial = DetalleTransaccion.objects.all().filter(transaction_id=detalle_transaccions)
    codigo = HistorialMedicamento.objects.all()
    
    context = {
        'title':'Detalle de la transaccion {}'.format(detalle_transaccions),
        'historial_list': detalle_transaccions,
        'detalle_historial':detalles_historial,
        'codigo':codigo,
    }
    return render(request, 'transactions/detail.html', context)


#--- LISTAR ENTRADAS Y SALIDAS
@login_required
def listar_transacciones(request):
    historialTransaccion_list = HistorialTransaccion.objects.all().order_by('-id')
    entradas = HistorialTransaccion.objects.all().filter(transaction_type='Entrada').order_by('-id')
    salidas = HistorialTransaccion.objects.all().filter(transaction_type='Salida').order_by('-id')
    page_obj = paginacion(request,historialTransaccion_list)
    

    context = {
        'title':'Transacciones',
        'entradas_list': entradas,
        'salidas_list':salidas,   
        'page_obj':page_obj,     
    }
    return render(request, 'transactions/index.html', context)


#--- Editar Entradas y Salidas
@login_required
def editar_transacciones(request, id):
    transaccion = get_object_or_404(HistorialTransaccion, id=id)
    form = HistorialTransaccionForm(instance=transaccion)
    if request.method == 'POST':
        try:
            infor = request.body
            ver = json.loads(infor)
            validar = ver.get('validar')
            lista = ver.get('lista', [])            
            user_id = request.user.id        
            transaction_type = ver.get('transaction_type')
            transaction_date = ver.get('transaction_date')
            
            
            if validar:
                transaccion.transaction_type = transaction_type
                transaccion.transaction_date = transaction_date
                user = get_object_or_404(User, id=user_id)
                transaccion.user_id = user
                transaccion.total = 0
                transaccion.save()
                detalle_historial_transaccion = DetalleTransaccion.objects.all().filter(transaction_id=transaccion)
                for contenido in lista:
                    if(len(contenido) == len(detalle_historial_transaccion)):
                        print("Sigue la misma cantidad de seleccionados, pero pudo ver algun cambio, vamos a revisar")

                        for elemento, elemento2 in zip(contenido, detalle_historial_transaccion):
                            elemento2.transaction_id = transaccion
                            medicamento_id = get_object_or_404(Medicamento, id = elemento["medicine_id"])
                            elemento2.medicine_id = medicamento_id
                            elemento2.quantity = elemento["cantidad"]
                            elemento2.price = elemento["sale_price"]
                            elemento2.subtotal = 0
                            elemento2.save()

                    elif(len(contenido) < len(detalle_historial_transaccion)):
                        print("Se quito un elemento, vamos a revisar")
                        # Se eliminan todos los detalles de esta transaccion y se crea un nuevo detalle
                        detalle_historial_transaccion.delete()
                        for elementos in contenido:
                            nuevo_detalle = DetalleTransaccion()
                            medicamento_id = get_object_or_404(Medicamento, id = elementos["medicine_id"])
                            nuevo_detalle.transaction_id = transaccion
                            nuevo_detalle.medicine_id = medicamento_id
                            nuevo_detalle.quantity = elementos["cantidad"]
                            nuevo_detalle.price = elementos["sale_price"]
                            nuevo_detalle.subtotal = 0
                            nuevo_detalle.save()

                    elif(len(contenido) > len(detalle_historial_transaccion)):
                        print("Se agrego un nuevo elemento, vamos agregarlo")
                        # Se eliminan todos los detalles de esta transaccion y se crea un nuevo detalle
                        detalle_historial_transaccion.delete()
                        for elementos in contenido:
                            nuevo_detalle = DetalleTransaccion()
                            medicamento_id = get_object_or_404(Medicamento, id = elementos["medicine_id"])
                            nuevo_detalle.transaction_id = transaccion
                            nuevo_detalle.medicine_id = medicamento_id
                            nuevo_detalle.quantity = elementos["cantidad"]
                            nuevo_detalle.price = elementos["sale_price"]
                            nuevo_detalle.subtotal = 0
                            nuevo_detalle.save()
                        
                
                response_data = {'mensaje': 'Datos recibidos correctamente'}
                
                return JsonResponse(response_data)
            return redirect('transactions:realizar_transaccion')

        except ValueError:
            print('DECODING JSON HAS FAILED')
    context = {
        'title':'Editar {}'.format(transaccion),
        'form':form,
        'medicines': informacion_completa_medicamento(),
        'user':request.user,
        'user_id':request.user.id,
        'transaccion':transaccion
    }
    return render(request, 'transactions/forms/update.html', context)


#---- CREAR ENTRADAS Y SALIDAS 
@login_required
def agregar_transaccion(request):
    if request.method == 'POST':
        try:
            infor = request.body
            ver = json.loads(infor)
            validar = ver.get('validar')
            lista = ver.get('lista', [])
            print(ver)
            user_id = request.user.id        
            transaction_type = ver.get('transaction_type')
            transaction_date = ver.get('transaction_date')
            
            
            if validar:
                transaccion = HistorialTransaccion()
                transaccion.transaction_type = transaction_type
                transaccion.transaction_date = transaction_date
                user = get_object_or_404(User, id=user_id)
                transaccion.user_id = user
                transaccion.total = 0
                transaccion.save()
                
                for contenido in lista:
                    for elementos in contenido:
                        #{'cantidad': '1', 'medicine_id': 15, 'sale_price': '5.50'}
                        
                        detalle_transaccion = DetalleTransaccion()   
                        transaccion_id = get_object_or_404(HistorialTransaccion, id=transaccion.id)                 
                        medicamento_id = get_object_or_404(Medicamento, id = elementos["medicine_id"])
                        
                        detalle_transaccion.transaction_id = transaccion_id
                        detalle_transaccion.medicine_id = medicamento_id
                        detalle_transaccion.quantity = elementos["cantidad"]
                        detalle_transaccion.price = elementos["sale_price"]
                        detalle_transaccion.subtotal = 0
                        detalle_transaccion.save()
                
                response_data = {'mensaje': 'Datos recibidos correctamente'}
                
                return JsonResponse(response_data)
            return redirect('transactions:realizar_transaccion')

        except ValueError:
            print('DECODING JSON HAS FAILED')
            


    context = {
        'title':'Realizar Transaccion',
        'form':HistorialTransaccionForm,
        'user':request.user,
        'user_id':request.user.id,
        'medicines': informacion_completa_medicamento(),
    }
    return render(request, 'transactions/forms/add.html', context)