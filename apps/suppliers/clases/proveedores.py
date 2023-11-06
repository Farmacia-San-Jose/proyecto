import json

class Proveedor:
    contador = 0
    def __init__(self, id, first_name, last_name,company = None,telephone=None, email=None):
        Proveedor.contador+=1
        self._contador = Proveedor.contador
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._company = company
        self._telephone = telephone
        self._email = email

        self._supplier_dic = {}
    
    @property
    def contadorRegistro(self):
        return self._contador
    
    @property
    def id(self):
        return self._id
    
    @property
    def full_name(self):
        if self._first_name is None:
            return '{}'.format(self._last_name)
        elif self._last_name is None:
            return '{}'.format(self._first_name)
        else:
            return '{} {}'.format(self._first_name, self._last_name)
    
    @property
    def company(self):
        return self._company
    
    @property
    def telephone(self):
        return self._telephone
    
    @property
    def email(self):
        return self._email
    
    @property
    def diccionario(self):
        self._supplier_dic['id']=self.id
        self._supplier_dic['full_name']=self.full_name
        self._supplier_dic['company']=self.company
        self._supplier_dic['telephone']=self.telephone
        self._supplier_dic['email']=self.email

        return self._supplier_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)
        