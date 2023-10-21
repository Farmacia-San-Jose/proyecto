from django.db import models

# MODELS
from apps.medicines.models import Medicamento

# Create your models here.
class Ubicacion(models.Model):
    type_location = models.CharField(max_length=150, blank=False,null=False)


    def __str__(self):
        return self.type_location

class Seccion(models.Model):
    location_section = models.CharField(max_length=50)

    def __str__(self):
        return self.location_section

class HistorialInvetario(models.Model):
    medicine_id = models.ForeignKey(Medicamento, blank=False, null=False, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Ubicacion, blank=True, null=True, on_delete=models.CASCADE)
    quantity_stock = models.IntegerField()
    row = models.CharField(max_length=50)
    column = models.CharField(max_length=50)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    locationsection_id = models.ForeignKey(Seccion, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.medicine_id)

