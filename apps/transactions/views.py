# URL
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required

# MODELS
from .models import HistorialTransaccion, DetalleTransaccion
from apps.medicines.models import Medicamento
from apps.users.models import User

# FORMULARIO
from .forms import HistorialTransaccionForm

# LISTADO DE INFORMACION UNIDA
from apps.medicines.consultas.unir_datos import informacion_completa_medicamento
# Create your views here.

import json
from django.http import JsonResponse

@login_required
def agregar_transaccion(request):
    if request.method == 'POST':
        try:
            infor = request.body
            ver = json.loads(infor)
            print(ver)
            validar = ver.get('validar')
            lista = ver.get('lista', [])
            user_id = request.user.id        
            transaction_type = ver.get('transaction_type')
            transaction_date = ver.get('transaction_date')
            
            if validar:
                for contenido in lista:
                    for elementos in contenido:
                        #{'cantidad': '1', 'medicine_id': 15, 'sale_price': '5.50'}
                        transaccion = HistorialTransaccion()

                        transaccion.transaction_type = transaction_type
                        transaccion.transaction_date = transaction_date
                        user = get_object_or_404(User, id=user_id)
                        transaccion.user_id = user
                        transaccion.total = 0
                        transaccion.save()




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