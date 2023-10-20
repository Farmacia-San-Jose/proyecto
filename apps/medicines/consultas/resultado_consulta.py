# Conecction
from django.db import connection
import json
import requests

# CONSULTAS
from .consulta import LISTADOMEDICAMENTO, LISTADOCLASIFICACION, LISTADOHISTORIALMEDICAMENTO, LISTADOHISTORIALINVENTARIO
from .consulta import listado_completo_medicamentos, listado_medicamento_existencia, listado_medicamento_vencido

# CLASES
from ..clases.medicamentos import Medicamento, HistorialMedicamento
from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.locations.clases.ubicaciones import Ubicacion, Seccion, HistorialInventario
from apps.suppliers.clases.proveedores import Proveedor
from apps.presentations.clases.presentaciones import Presentacion

# RECURSOS
from .recurso import clasifications,historial_medicamento, inventory

def listar_f():
    listado_general = []
    consulta_listado_medicamento = LISTADOMEDICAMENTO+';'
    
    consulta_listado_historial_medicamento = LISTADOHISTORIALMEDICAMENTO+' WHERE H.medicine_id_id = %s'+';'
    consulta_listado_historial_inventario = LISTADOHISTORIALINVENTARIO+' WHERE HI.medicine_id_id = %s'+';'
    consulta_listado_clasificacion = LISTADOCLASIFICACION+';'
    contador =0
    
    

    with connection.cursor() as cursor:
        medicamento_list = []
        cursor.execute(consulta_listado_medicamento)
        resultado = cursor.fetchall()
        

        for medicamento in resultado:
            medi = Medicamento(medicamento[0],medicamento[1],medicamento[2],medicamento[3])
            medicamento_list.append(medi)
        
        for medicina in medicamento_list:
            
            cursor.execute(consulta_listado_clasificacion)
            resultado = cursor.fetchall()
            clasificacion = clasifications(resultado,medicina.id)
            

            

            cursor.execute(consulta_listado_historial_medicamento, str(medicina.id))
            resultado = cursor.fetchall()
            
            historialM= historial_medicamento(resultado,medicina)

            cursor.execute(consulta_listado_historial_inventario, str(medicina.id))
            resultado = cursor.fetchall()

            historialI = inventory(resultado,medicina)
            contador+=1

            medicamento_dic = {
                'contador':contador,
                'medicines':medicina.diccionario,
                'clasificacion':clasificacion,
                'historial_medicamento':historialM,
                'historial_inventario':historialI
            }

            listado_general.append(medicamento_dic)
    return listado_general

def listar():
    medicamento_list=[]

    with connection.cursor() as cursor:
        cursor.execute(listado_completo_medicamentos)    
        resultados = cursor.fetchall()
        for resul in resultados:
            medicamentos ={
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_list.append(medicamentos)
    return medicamento_list

def existencia():
    medicamento_existencia = []
    contar = 0
    

    with connection.cursor() as cursor:
        cursor.execute(listado_medicamento_existencia)    
        resultados = cursor.fetchall()
        for resul in resultados:
            contar +=1    
            medicamentos ={
                'contador':contar,
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_existencia.append(medicamentos)
    return medicamento_existencia

def vencidos():
    medicamento_vencido = []
    contar =0
    with connection.cursor() as cursor:
        cursor.execute(listado_medicamento_vencido)    
        resultados = cursor.fetchall()
        
        
        for resul in resultados:
            contar+=1  
                
            medicamentos ={
                'contador':contar,
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_vencido.append(medicamentos)
    return medicamento_vencido