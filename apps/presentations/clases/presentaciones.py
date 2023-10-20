import json

class Presentacion:
    contador = 0
    def __init__(self, id,presentation_type,description=None):
        Presentacion.contador+=1
        self._contador = Presentacion.contador
        self._id = id
        self._presentation_type = presentation_type
        self._description = description
        self._presentation_dic = {}

    @property
    def id(self):
        return self._id
    
    @property
    def contadorRegistro(self):
        return self._contador
    
    @property
    def tipo_presentacion(self):
        return self._presentation_type
    
    @property
    def description(self):
        return self._description
    
    @property
    def diccionario(self):
        self._presentation_dic['id']=self.id
        self._presentation_dic['presentation_type']=self.tipo_presentacion
        self._presentation_dic['description'] = self.description
        return self._presentation_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)
    