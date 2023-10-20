import json

class Ubicacion:
    contador = 0
    def __init__(self, id,type_location):
        Ubicacion.contador +=1

        self._contador = Ubicacion.contador
        self._id = id
        self._type_location = type_location
        self._ubicacion_dic = {}

    @property
    def contadorRegistro(self):
        return self._contador

    @property
    def id(self):
        return self._id
    
    @property
    def type_location(self):
        return self._type_location
    
    @property
    def diccionario(self):
        self._ubicacion_dic['id']=self.id
        self._ubicacion_dic['type_location'] = self.type_location
        return self._ubicacion_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)
    
class Seccion:
    contador = 0

    def __init__(self, id, location_section):
        Seccion.contador +=1
        self._contador = Ubicacion.contador
        self._id = id
        self._location_section = location_section
        self._seccion_dic = {}
    
    @property
    def contadorRegistro(self):
        return self._contador
    
    @property
    def id(self):
        return self._id
    
    @property
    def location_section(self):
        return self._location_section
    
    @property
    def diccionario(self):
        self._seccion_dic['id']=self.id
        self._seccion_dic['location_section'] = self.location_section
        return self._seccion_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)

class HistorialInventario:
    contador = 0
    def __init__(self,id,section_id, location_id,medicine_id, quantity_stock = None, row =None, column=None, sale_price =None ):
        HistorialInventario.contador+=1
        self._contador = HistorialInventario.contador
        
        self._id = id
        self._section_id = section_id
        self._location_id = location_id
        self._medicine_id = medicine_id
        self._quantity_stock=quantity_stock
        self._row = row
        self._column=column
        self._sale_price = sale_price
        self._historial_dic = {}
    
    @property
    def contadorRegistro(self):
        return self._contador
    
    @property
    def id(self):
        return self._id
    
    @property
    def section_id(self):
        return self._section_id.diccionario
    
    @property
    def location_id(self):
        return self._location_id.diccionario
    
    @property
    def medicine_id(self):
        return self._medicine_id.diccionario
    
    @property
    def quantity_stock(self):
        return self._quantity_stock
    
    @property
    def row(self):
        return self._row
    
    @property
    def column(self):
        return self._column
    
    @property
    def sale_price(self):
        return self._sale_price
    
    @property
    def diccionario(self):
        self._historial_dic['id']=self.id
        #self._historial_dic['medicine_id']=self.medicine_id
        self._historial_dic['location_id']=self.location_id
        self._historial_dic['section_id']=self.section_id
        self._historial_dic['quantity_stock']=self.quantity_stock
        self._historial_dic['row']=self.row
        self._historial_dic['column']=self.column
        self._historial_dic['sale_price']=self.sale_price

        return self._historial_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)
    

    

    

