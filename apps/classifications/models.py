from django.db import models

# MODELS
from apps.medicines.models import Medicamento

# Create your models here.
class UsoTerapeutico(models.Model):
    type_therepeuticuse = models.CharField(max_length=150,blank=False, null=False, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_therepeuticuse

class FormaAdministracion(models.Model):
    type_adminstrationform = models.CharField(max_length=150,blank=False,null=False,unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type_adminstrationform
    

class Clasificacion(models.Model):
    medicine_id = models.ForeignKey(Medicamento, blank=False,null=False,on_delete=models.CASCADE)
    therepeuticuse_id = models.ForeignKey(UsoTerapeutico, blank=True,null=True,on_delete=models.CASCADE)
    formadministration_id = models.ForeignKey(FormaAdministracion, blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.medicine_id}'
    