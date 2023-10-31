# CONSULTAS PARA LA BASE DE DATOS
from .consulta import LISTADOMEDICAMENTO, LISTADOCLASIFICACION, LISTADOHISTORIALMEDICAMENTO, LISTADOHISTORIALINVENTARIO

# CLASES
from apps.classifications.clases.clasificaciones import Clasificacion, FormaAdministracion, UsoTerapeutico
from apps.locations.clases.ubicaciones import Ubicacion, Seccion, HistorialInventario
from apps.medicines.clases.medicamentos import Medicamento, HistorialMedicamento
from apps.presentations.clases.presentaciones import Presentacion
from apps.suppliers.clases.proveedores import Proveedor


# Conecction
from django.db import connection

# JSON
import json



# FUNCION PARA UNIR LA INFORMACION COMPLETA DEL MEDICAMENTO
def informacion_completa_medicamento():
    # VARIABLES
    listado_completo =[]   
    listado_medicamento = LISTADOMEDICAMENTO+';'
    
    with connection.cursor() as cursor:
        medicamento_list = []
        cursor.execute(listado_medicamento)
        resultado = cursor.fetchall()

        for medicamento in resultado:
            # Guardar toda la informacion de medicamento
            medi = Medicamento(medicamento[0], medicamento[1], medicamento[2])            
            medicamento_list.append(medi)
        
        for medic in medicamento_list:
            diccionario_datos={}
            # Medicamento
            diccionario_datos['medicines']= medic.diccionario
            # Historial del medicamento
            diccionario_datos['historial_medicamento'] = historial_medicamento(medic.id)

            # Historial de Inventario
            diccionario_datos['hisotrial_inventario'] = historial_inventario(medic.id)
            
            # Segun su Clasificacion
            diccionario_datos['clasificacion'] = clasificacion(medic.id)

            listado_completo.append(diccionario_datos)
        
        
        return listado_completo
        
        


    

# Lista el historial del medicamento segun el medicamento
def historial_medicamento(id):
       historial_medicamento = '{} WHERE H.medicine_id_id = {};'.format(LISTADOHISTORIALMEDICAMENTO, id)
       with connection.cursor() as cursor:
            cursor.execute(historial_medicamento)
            resultado = cursor.fetchall()

            for historial_m in resultado:
                supplier = Proveedor(historial_m[1], historial_m[2], historial_m[3], historial_m[4], historial_m[5], historial_m[6])
                presentation = Presentacion(historial_m[7], historial_m[8], historial_m[9])
                historialM = HistorialMedicamento(historial_m[0],id, supplier, presentation, historial_m[10], historial_m[11], historial_m[12], historial_m[13])

                return historialM.diccionario

# Lista el historial de inventario segun el medicamento 
def historial_inventario(id):
    historial_inventario ='{} WHERE HI.medicine_id_id = {};'.format(LISTADOHISTORIALINVENTARIO, id)
    with connection.cursor() as cursor:
            cursor.execute(historial_inventario)
            resultado = cursor.fetchall()

            for historial_i in resultado:
                location = Ubicacion(historial_i[3], historial_i[4])
                section =  Seccion(historial_i[1], historial_i[2])
                historialI = HistorialInventario(historial_i[0],section,location,id, historial_i[5], historial_i[6], historial_i[7], historial_i[8])

                return historialI.diccionario

def clasificacion(id):
    clasificacion = '{} WHERE C.medicine_id_id = {};'.format(LISTADOCLASIFICACION, id)
    clasifications = []
    with connection.cursor() as cursor:
            cursor.execute(clasificacion)
            resultado = cursor.fetchall()

            for clasifi in resultado:
                uso_terapeutico = UsoTerapeutico(clasifi[4], clasifi[5], clasifi[6])
                forma_administracion = FormaAdministracion(clasifi[1], clasifi[2], clasifi[3])
                clasifica = Clasificacion(clasifi[0],id,uso_terapeutico,forma_administracion)
                clasifications.append(clasifica.diccionario)
    return clasifications