import json

class UsoTerapeutico:
  contador = 0
  def __init__(self, id,type_therepeuticuse, description=None):
    UsoTerapeutico.contador += 1
    self._contador = UsoTerapeutico.contador
    self._id = id
    self._type_therepeuticuse = type_therepeuticuse
    self._description = description
    self._uso_dic = {}
  
  @property
  def contadorRegistro(self):
    return self._contador
  
  @property
  def id(self):
    return self._id
  
  @property
  def type_therepeuticuse(self):
    return self._type_therepeuticuse
  
  @property
  def description(self):
    return self._description
  
  @property
  def diccionario(self):
    self._uso_dic['id']=self.id
    self._uso_dic['type_therepeuticuse']=self.type_therepeuticuse
    self._uso_dic['description']=self.description
    return self._uso_dic
  
  def __str__(self):
    uso_dic = {
        'id': self.id,
        'type_therepeuticuse': self.type_therepeuticuse,
        'description': self.description
    }
    return json.dumps(uso_dic)



class FormaAdministracion:
  contador = 0
  def __init__(self, id,type_administrationform, description=None):
    FormaAdministracion.contador += 1
    self._contador = FormaAdministracion.contador
    self._id = id
    self._type_administrationform = type_administrationform
    self._description = description
    self._forma_dic = {}
  
  @property
  def contadorRegistro(self):
    return self._contador
  
  @property
  def id(self):
    return self._id

  @property
  def type_administrationform(self):
    return self._type_administrationform

  @property
  def description(self):
    return self._description
  
  @property
  def diccionario(self):
    self._forma_dic['id']=self.id
    self._forma_dic['type_administrationform']=self.type_administrationform
    self._forma_dic['description']=self.description
    return self._forma_dic

  def __str__(self):
    forma_dic = {
        'id': self.id,
        'type_administrationform': self.type_administrationform,
        'description': self.description
    }
    return json.dumps(forma_dic)


class Clasificacion:
  contador = 0
    

  def __init__(self,id,medicines_id,type_therepeuticuse_id=None,type_administrationform_id=None):
    Clasificacion.contador += 1
    self._contador = Clasificacion.contador
    self._id = id
    self._clasificacion_dic = {}


    # ---------- ID MEDICAMENTO
    self._medicines_id = medicines_id

    # -------- Forma de administracion

    if type_administrationform_id is None:
      type_administrationform_id = []


    self._type_administrationform_id = type_administrationform_id


    # ----------- FORMA DE ADMINISTRACION
    if type_therepeuticuse_id is None:
      type_therepeuticuse_id = []


    self._type_therepeuticuse_id = type_therepeuticuse_id


# ------ METODOS GET
  

  @property
  def id(self):
    return self._id
  
  @property
  def contadorRegistro(self):
    return self._contador

  @property
  def medicines_id(self):
    return self._medicines_id.diccionario
  


  @property
  def forma_administracion(self):
    listF = []
    for forma in self._type_administrationform_id:
      forma_dic = {
          'id': forma.id,
          'type_administrationform': forma.type_administrationform,
          'description': forma.description
      }
      listF.append(forma_dic)
      

    return listF
  
  @property
  def diccionario(self):
    
    self._clasificacion_dic['id'] = self.id
    #self._clasificacion_dic['medicines'] = self.medicines_id
    self._clasificacion_dic['forma_administracion']=self.forma_administracion
    self._clasificacion_dic['uso_terapeutico']=self.uso_terapeutico

    return self._clasificacion_dic



  @property
  def uso_terapeutico(self):
    listU = []
    for uso in self._type_therepeuticuse_id:
      use_dic = {
          'id': uso.id,
          'type_therepeuticuse': uso.type_therepeuticuse,
          'description': uso.description
      }
      listU.append(use_dic)
      
      
    return listU


# ---------- METODOS

  def agregar_forma_administracion(self, type_administrationform):
    self._type_administrationform_id.append(type_administrationform)

  def agregar_uso_terapeeutico(self, type_therepeuticuse):
    self._type_therepeuticuse_id.append(type_therepeuticuse)


  def __str__(self):
    
    return json.dumps(self.diccionario, indent=4)
