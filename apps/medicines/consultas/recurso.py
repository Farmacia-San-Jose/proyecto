# CLASES
from ..clases.medicamentos import Medicamento, HistorialMedicamento
from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.locations.clases.ubicaciones import Ubicacion, Seccion, HistorialInventario
from apps.suppliers.clases.proveedores import Proveedor
from apps.presentations.clases.presentaciones import Presentacion

import json
    

def clasifications(resultado,id):
    
    listado_general = []
    listado_clasificacion = []
    list_forma =[]
    list_uso = []
    id = id
    for clasificar in resultado:
        forma = FormaAdministracion(clasificar[1],clasificar[2],clasificar[3])
        uso = UsoTerapeutico(clasificar[4],clasificar[5],clasificar[6])
        list_forma.append(forma.diccionario)
        list_uso.append(uso.diccionario)


        diccionario = {
            'clasificacion_id':clasificar[0],
            'medicina_id':clasificar[7],
            'forma_id':list_forma,
            'uso_id':list_uso
        }
        listado_clasificacion.append(diccionario)

    result = [elemento for elemento in listado_clasificacion if elemento['medicina_id'] == id ]
    listado_general.append(result)
    return listado_general
    
           

        

def inventory(resultado,medicina):
    for historial_invetario in resultado:
        seccion = Seccion(historial_invetario[1],historial_invetario[2])
        ubicacion = Ubicacion(historial_invetario[3],historial_invetario[4])
        inventario = HistorialInventario(historial_invetario[0],seccion,ubicacion,medicina,historial_invetario[5],historial_invetario[6],historial_invetario[7],historial_invetario[8])
        return inventario.diccionario
   

def historial_medicamento(resultado,medicina):
    
    for historial_medicamento in resultado:
        proveedor = Proveedor(historial_medicamento[1],historial_medicamento[2], historial_medicamento[3],historial_medicamento[4],historial_medicamento[5],historial_medicamento[6])
        
        presentacion = Presentacion(historial_medicamento[7],historial_medicamento[8],historial_medicamento[9])

        medicamento_historial = HistorialMedicamento(historial_medicamento[0],medicina,proveedor,presentacion, historial_medicamento[10], historial_medicamento[11], historial_medicamento[12], historial_medicamento[13])

        
        return medicamento_historial.diccionario
