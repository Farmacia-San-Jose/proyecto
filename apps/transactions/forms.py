# Creacion de formulario
from django import forms
# Tiempo
from datetime import datetime
# Modelos
from apps.transactions.models import HistorialTransaccion, DetalleTransaccion

class HistorialTransaccionForm(forms.ModelForm):
    class Meta:
        model = HistorialTransaccion
        fields = [
            'transaction_type',
            'transaction_date',
            'user_id'

        ]

        labels = {
            'transaction_type': 'Tipo de transaccion',
            'transaction_date': 'Fecha de transaccion',   
            'user_id':'Usuario'

        }

        widgets = {
            'transaction_type': forms.Select(attrs ={'class':'form-control', 'name':'transaction_type', 'id':'transaction_type', 'style':'border:1px solid #52be80; '}),
            'transaction_date': forms.DateInput(format='%Y-%m-%d', attrs = {'value': datetime.now().strftime('%Y-%m-%d'),
                'class':'form-control', 'name':'transaction_date', 'id':'transaction_date', 'type':'date','style':'border:1px solid #52be80; '
            }),
            'user_id':forms.TextInput(attrs={'class':'form-control','id':'user_id','disabled':'disabled', 'style':'border:1px solid #52be80;'})
            
        }

