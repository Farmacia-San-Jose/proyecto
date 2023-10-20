from django.db import models

# Models
from apps.suppliers.models import Proveedor
from apps.presentations.models import Presentacion
# Create your models here.

class Medicamento(models.Model):
    medicine_name = models.CharField(max_length=150, null=False,blank=False)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name


class HistorialMedicamento(models.Model):
    medicine_id = models.ForeignKey(Medicamento, blank=False, null=False, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Proveedor, blank=False, null=False, on_delete=models.CASCADE)
    presentation_id = models.ForeignKey(Presentacion, blank=False, null=False, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    brand = models.CharField(max_length=150, blank=True, null=True)
    medication_code = models.CharField(max_length=25, blank=True, null=True)
    expiration_date = models.DateField()


    def __str__(self):
        return '{} {} {} {}'.format(self.medicine_id, self.supplier_id, self.presentation_id, self.expiration_date)
