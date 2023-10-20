from django.db import models

# MODELS
from apps.users.models import User
from apps.medicines.models import Medicamento

# Create your models here.
class HistorialTransaccion(models.Model):
    transaction = [
        ('Entrada','Entrada'),
        ('Salida','Salida')
    ]
    transaction_type = models.CharField(choices=transaction, default='Entrada', null=False, blank=False, max_length=150)
    transaction_date = models.DateField()
    user_id = models.ForeignKey(User, related_name='users',blank=False,null=False, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    

    def __str__(self) :
        return '{} {} {}'.format(self.transaction_type, self.user_id, self.transaction_date)
    
class DetalleTransaccion(models.Model):
    transaction_id = models.ForeignKey(HistorialTransaccion, related_name='transactions',blank=False, null=False, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicamento, null=False, related_name='medicines',blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self) :
        return '{} {}'.format(self.transaction_id, self.medicine_id)
