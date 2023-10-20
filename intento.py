from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.medicines.clases.medicamentos import Medicamento
import json

if __name__ == '__main__':
    
    list_general = []
    list_medicamento = []
    contarClasificacion = 0


    list_medicamento.append(Medicamento(1,'Acetaminofen'))
    list_medicamento.append(Medicamento(2,'Ibuprofeno'))

    for medicamento in list_medicamento:
        
        contarClasificacion +=1

        clasificacion = Clasificacion(contarClasificacion, medicamento)

        me ={
            'medicines':medicamento.diccionario,
            'clasificacion':clasificacion.diccionario
        }

        list_general.append(me)
    consulta ="""
SELECT 
C.id AS 'classification_id',
F.id AS 'forma_id',
F.type_adminstrationform AS 'forma_administracion',
F.description AS 'description',
U.id AS 'uso_id',
U.type_therepeuticuse AS 'uso_terapeutico',
U.description AS 'description'
FROM classifications_clasificacion AS C
INNER JOIN classifications_formaadministracion AS F ON F.id = C.formadministration_id_id
INNER JOIN classifications_usoterapeutico AS U ON U.id = C.therepeuticuse_id_id
INNER JOIN medicines_medicamento AS M ON M.id = C.medicine_id_id"""
    consulta+=';'
    print(consulta)
    

    